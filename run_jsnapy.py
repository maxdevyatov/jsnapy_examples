from jnpr.jsnapy import SnapAdmin

js = SnapAdmin()



def call_jsnap(test_file):
 
  failed_flag = False

  chk = js.snapcheck(test_file)

  for check in chk:
    for test in check.test_details:
      for subtest in check.test_details[test]:
        for item in subtest['failed']:
          failed_flag = True
          print check.device, "FAILED TEST:", test, item['id'],  item['post'], "Expected:",subtest['testoperation'], (subtest['expected_node_value'] if 'expected_node_value' in subtest else subtest['node_name'])

  if failed_flag:
    return True
  else:
    return False


print "************************************************************"
print "************************************************************"
print "************************************************************"

if call_jsnap("main_test1.yml"):
  print "############################################################"
  print "#                    SOME TESTS FAILED                     #"
  print "############################################################"
else:
  print "############################################################"
  print "#                     ALL TESTS PASSED                     #"
  print "############################################################"
print "************************************************************"
print "************************************************************"
print "************************************************************"
