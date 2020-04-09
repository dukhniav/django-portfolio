<?php
    // Check for submit
    if(filter_has_var(INPUT_POST, 'submit')){
        echo 'Submitted';
    }
    // if(isset($_POST['submit'])) {
    //     mail("artem.dukhnitskiy@gmail.com", "Form to email message", $_POST["message"], "From: an@email.address");

    //     // $to = "artem.dukhnitskiy@gmail.com";
    //     // $subject = "Contact page";
    //     // $name_field = $_POST['name'];
    //     // $email_field = $_POST['email'];
    //     // $message = $_POST['message'];
        
    //     // foreach($_POST['human'] as $human_value) {
    //     //     $check_message .= "Checked: $human_value\n";
    //     // }
        
    //     // $robot = $_POST['robot'];
        
    //     // $body = "From: $name_field\n E-Mail: $email_field\n Human: $human\n Robot: $robot\n Message:\n $message";
        
    //     // echo "Message sent!";
    //     // mail($to, $subject, $body);
    // } else {
    //     echo "blarg!";
    // }
?>