; Auto-generated. Do not edit!


(cl:in-package cs1567p1-srv)


;//! \htmlinclude MakeNewMaze-request.msg.html

(cl:defclass <MakeNewMaze-request> (roslisp-msg-protocol:ros-message)
  ((cols
    :reader cols
    :initarg :cols
    :type cl:integer
    :initform 0)
   (rows
    :reader rows
    :initarg :rows
    :type cl:integer
    :initform 0))
)

(cl:defclass MakeNewMaze-request (<MakeNewMaze-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MakeNewMaze-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MakeNewMaze-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<MakeNewMaze-request> is deprecated: use cs1567p1-srv:MakeNewMaze-request instead.")))

(cl:ensure-generic-function 'cols-val :lambda-list '(m))
(cl:defmethod cols-val ((m <MakeNewMaze-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:cols-val is deprecated.  Use cs1567p1-srv:cols instead.")
  (cols m))

(cl:ensure-generic-function 'rows-val :lambda-list '(m))
(cl:defmethod rows-val ((m <MakeNewMaze-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:rows-val is deprecated.  Use cs1567p1-srv:rows instead.")
  (rows m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MakeNewMaze-request>) ostream)
  "Serializes a message object of type '<MakeNewMaze-request>"
  (cl:let* ((signed (cl:slot-value msg 'cols)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rows)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MakeNewMaze-request>) istream)
  "Deserializes a message object of type '<MakeNewMaze-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cols) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rows) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MakeNewMaze-request>)))
  "Returns string type for a service object of type '<MakeNewMaze-request>"
  "cs1567p1/MakeNewMazeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakeNewMaze-request)))
  "Returns string type for a service object of type 'MakeNewMaze-request"
  "cs1567p1/MakeNewMazeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MakeNewMaze-request>)))
  "Returns md5sum for a message object of type '<MakeNewMaze-request>"
  "15d28abd61347f29f8562c138de059b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MakeNewMaze-request)))
  "Returns md5sum for a message object of type 'MakeNewMaze-request"
  "15d28abd61347f29f8562c138de059b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MakeNewMaze-request>)))
  "Returns full string definition for message of type '<MakeNewMaze-request>"
  (cl:format cl:nil "int64 cols~%int64 rows~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MakeNewMaze-request)))
  "Returns full string definition for message of type 'MakeNewMaze-request"
  (cl:format cl:nil "int64 cols~%int64 rows~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MakeNewMaze-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MakeNewMaze-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MakeNewMaze-request
    (cl:cons ':cols (cols msg))
    (cl:cons ':rows (rows msg))
))
;//! \htmlinclude MakeNewMaze-response.msg.html

(cl:defclass <MakeNewMaze-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:integer
    :initform 0))
)

(cl:defclass MakeNewMaze-response (<MakeNewMaze-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MakeNewMaze-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MakeNewMaze-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<MakeNewMaze-response> is deprecated: use cs1567p1-srv:MakeNewMaze-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <MakeNewMaze-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:ok-val is deprecated.  Use cs1567p1-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MakeNewMaze-response>) ostream)
  "Serializes a message object of type '<MakeNewMaze-response>"
  (cl:let* ((signed (cl:slot-value msg 'ok)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MakeNewMaze-response>) istream)
  "Deserializes a message object of type '<MakeNewMaze-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'ok) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MakeNewMaze-response>)))
  "Returns string type for a service object of type '<MakeNewMaze-response>"
  "cs1567p1/MakeNewMazeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakeNewMaze-response)))
  "Returns string type for a service object of type 'MakeNewMaze-response"
  "cs1567p1/MakeNewMazeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MakeNewMaze-response>)))
  "Returns md5sum for a message object of type '<MakeNewMaze-response>"
  "15d28abd61347f29f8562c138de059b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MakeNewMaze-response)))
  "Returns md5sum for a message object of type 'MakeNewMaze-response"
  "15d28abd61347f29f8562c138de059b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MakeNewMaze-response>)))
  "Returns full string definition for message of type '<MakeNewMaze-response>"
  (cl:format cl:nil "int64 ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MakeNewMaze-response)))
  "Returns full string definition for message of type 'MakeNewMaze-response"
  (cl:format cl:nil "int64 ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MakeNewMaze-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MakeNewMaze-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MakeNewMaze-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MakeNewMaze)))
  'MakeNewMaze-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MakeNewMaze)))
  'MakeNewMaze-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakeNewMaze)))
  "Returns string type for a service object of type '<MakeNewMaze>"
  "cs1567p1/MakeNewMaze")