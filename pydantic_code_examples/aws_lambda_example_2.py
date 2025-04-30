 {test="skip" lint="skip"}
import sysconfig
print(sysconfig.get_config_var("EXT_SUFFIX"))
#> '.cpython-312-x86_64-linux-gnu.so'
