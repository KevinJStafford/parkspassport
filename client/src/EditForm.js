import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";

 const EditForm = ({handleEditAmenity}) => {

    return (
      <div className="form-field">
        <h1>Edit An Amenity</h1>
        <Formik 
        initialValues={{amenityname:''}}
        validate={values => {
            const errors = {};
            if (!values.amenityname) {
                errors.amenityname = 'Amenity name must be greater than 1 character';
            } 
            return errors;
        }}
        onSubmit={(values, {setSubmitting}) => {
            console.log(values)
            setTimeout(() => {
                fetch('http://localhost:5555/amenities${id}', {
                    method: "PATCH",
                    headers: {
                      "Content-type": "application/json",
                    },
                    body: JSON.stringify(values),
            }).then((r) => {
                if (r.ok) {
                    r.json().then((editedAmenity) => handleEditAmenity(editedAmenity))
                } else {
                    console.log('something went wrong')
                }
            })
                setSubmitting(false)}, 400)
                }}>
        {({ isSubmitting }) => (
        <Form>
            <Field
            type="text"
            name="amenityname"
            placeholder="Enter the amenity" />
            <ErrorMessage name="amenityname" component="div" />
            <button type="submit" disabled={isSubmitting}>
                Submit
                </button>
        </Form>
        )}
        </Formik>
    </div>
    )
 };

export default EditForm;