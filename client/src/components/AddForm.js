import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";

 const AddForm = ({handleAddAmenity}) => {

    return (
      <div className="form-field">
        <h1>Add An Amenity</h1>
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
                fetch('http://localhost:5555/amenities', {
                    method: "POST",
                    headers: {
                      "Content-type": "application/json",
                    },
                    body: JSON.stringify(values),
            }).then((r) => {
                if (r.ok) {
                    r.json().then((newAmenity) => handleAddAmenity(newAmenity))
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

export default AddForm;