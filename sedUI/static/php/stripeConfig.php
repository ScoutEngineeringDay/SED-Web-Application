<?php
require_once('vendor/autoload.php');

$stripe = array(
  "secret_key"      => "sk_test_iIX7K5Yv2bIePNxXIiHDEseL",
  "publishable_key" => "pk_test_92kS90THLx5tJ1giZLy7JIcO"
);

\Stripe\Stripe::setApiKey($stripe['secret_key']);
?>
