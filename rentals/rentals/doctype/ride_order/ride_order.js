// Copyright (c) 2026, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {

	},
});
frappe.ui.form.on("Ride Order",{
    onload(frm){
        console.log("running load...");
    },
    setup(frm){
        console.log("setup...")
    },
    refresh(frm){
        console.log("on refresh...")

        if(frm.doc.status !== "Accepted"){
            frm.add_custom_button("Accept", () => {
            //status => Accpeted
                frm.set_value("status", "Accepted");
            //save the form
                frm.save();
            // frappe.show_alert("It works!")
            })
            frm.add_custom_button("Accept", () => {
            //status => Accpeted
                frm.set_value("status", "Rejected");
            //save the form
                frm.save();
        },"Actions")
    }
    },
    status(frm) {
            console.log("status changed");
    }
});

// frappe.ui.form.on("Ride Order", {
//     refresh(frm) {

//         if (frm.doc.docstatus !== 1) {
//             return;
//         }

//         if (frm.doc.status !== "Accepted") {

//             frm.page.add_action_item(__("Accept"), () => {
//                 frm.set_value("status", "Accepted");
//                 frm.save("Update");
//             });

//             frm.page.add_action_item(__("Reject"), () => {
//                 frm.set_value("status", "Rejected");
//                 frm.save("Update");
//             });

//         }
//     }
// });