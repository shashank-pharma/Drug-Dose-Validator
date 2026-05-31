# %% [markdown]
# Claud_AI contributed project.
# 
# Drug Dose Validator — Custom Exception + try/except
# 
# CDSCO submission mein dose validation critical hai — galat dose se patient safety risk hota hai. Ek custom exception banao DoseError. Phir ek class banao DoseValidator jisme method ho validate(drug_name, dose_mg, max_dose). Agar dose string ho toh TypeError raise karo. Agar dose 0 ya negative ho toh ValueError raise karo. Agar dose max_dose se zyada ho toh DoseError raise karo. Logging se saare errors "dose_errors.txt" mein save karo. 5 cases test karo.

# %%
import logging
logging.basicConfig(filename="dose_error.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

#making a custom exception
class DoseError(Exception):
    pass

#making the class which directly taking the parameters and verifying results
class DoseValidate:
    def validate(self,drug_name,dose_mg,max_dose):
        print(f"VALIDATING {drug_name} - {dose_mg}mg")

        try:
            if not isinstance(dose_mg,(int,float)):
                raise TypeError(f"Dose must be a number,got {type(dose_mg).__name__}")

            #negative checking
            if dose_mg <= 0:
                raise ValueError(f"Dose must be a positive number, got {dose_mg}")

            #checking for maximum dose
            if dose_mg > max_dose:
                raise DoseError(f"Dose exceeds maximum recommended dose of {max_dose}mg")

            print(f"{drug_name}-{dose_mg}mg is VALID")
            logging.info(f"{drug_name}-{dose_mg}mg is PASSED")

        except TypeError as e:
            print(f"ERROR: {e}")
            logging.error(f"{drug_name}-{dose_mg}mg is FAILED - {e}")

        except ValueError as e:
            print(f"ERROR: {e}")
            logging.error(f"{drug_name}-{dose_mg}mg is FAILED - {e}")

        except DoseError as e:
            print(f"ERROR: {e}")
            logging.error(f"{drug_name}-{dose_mg}mg is FAILED - {e}")

v = DoseValidate()
v.validate("Insulin",30,40)

v.validate("Semaglutide",500,250)

v.validate("Cetriziene","ten",10)

v.validate("Acetazolamide", 250, 250)

v.validate("Carbamazapine", -100, 800)





