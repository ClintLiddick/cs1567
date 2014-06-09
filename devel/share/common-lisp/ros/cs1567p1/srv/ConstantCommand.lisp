; Auto-generated. Do not edit!


(cl:in-package cs1567p1-srv)


;//! \htmlinclude ConstantCommand-request.msg.html

(cl:defclass <ConstantCommand-request> (roslisp-msg-protocol:ros-message)
  ((cmd
    :reader cmd
    :initarg :cmd
    :type geometry_msgs-msg:Twist
    :initform (cl:make-instance 'geometry_msgs-msg:Twist)))
)

(cl:defclass ConstantCommand-request (<ConstantCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConstantCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConstantCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<ConstantCommand-request> is deprecated: use cs1567p1-srv:ConstantCommand-request instead.")))

(cl:ensure-generic-function 'cmd-val :lambda-list '(m))
(cl:defmethod cmd-val ((m <ConstantCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:cmd-val is deprecated.  Use cs1567p1-srv:cmd instead.")
  (cmd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConstantCommand-request>) ostream)
  "Serializes a message object of type '<ConstantCommand-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cmd) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConstantCommand-request>) istream)
  "Deserializes a message object of type '<ConstantCommand-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cmd) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConstantCommand-request>)))
  "Returns string type for a service object of type '<ConstantCommand-request>"
  "cs1567p1/ConstantCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConstantCommand-request)))
  "Returns string type for a service object of type 'ConstantCommand-request"
  "cs1567p1/ConstantCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConstantCommand-request>)))
  "Returns md5sum for a message object of type '<ConstantCommand-request>"
  "304dd3f6ef6b49ed507d4f75dde10aeb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConstantCommand-request)))
  "Returns md5sum for a message object of type 'ConstantCommand-request"
  "304dd3f6ef6b49ed507d4f75dde10aeb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConstantCommand-request>)))
  "Returns full string definition for message of type '<ConstantCommand-request>"
  (cl:format cl:nil "geometry_msgs/Twist cmd~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConstantCommand-request)))
  "Returns full string definition for message of type 'ConstantCommand-request"
  (cl:format cl:nil "geometry_msgs/Twist cmd~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConstantCommand-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cmd))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConstantCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ConstantCommand-request
    (cl:cons ':cmd (cmd msg))
))
;//! \htmlinclude ConstantCommand-response.msg.html

(cl:defclass <ConstantCommand-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:integer
    :initform 0))
)

(cl:defclass ConstantCommand-response (<ConstantCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConstantCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConstantCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cs1567p1-srv:<ConstantCommand-response> is deprecated: use cs1567p1-srv:ConstantCommand-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <ConstantCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cs1567p1-srv:ok-val is deprecated.  Use cs1567p1-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConstantCommand-response>) ostream)
  "Serializes a message object of type '<ConstantCommand-response>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConstantCommand-response>) istream)
  "Deserializes a message object of type '<ConstantCommand-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConstantCommand-response>)))
  "Returns string type for a service object of type '<ConstantCommand-response>"
  "cs1567p1/ConstantCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConstantCommand-response)))
  "Returns string type for a service object of type 'ConstantCommand-response"
  "cs1567p1/ConstantCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConstantCommand-response>)))
  "Returns md5sum for a message object of type '<ConstantCommand-response>"
  "304dd3f6ef6b49ed507d4f75dde10aeb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConstantCommand-response)))
  "Returns md5sum for a message object of type 'ConstantCommand-response"
  "304dd3f6ef6b49ed507d4f75dde10aeb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConstantCommand-response>)))
  "Returns full string definition for message of type '<ConstantCommand-response>"
  (cl:format cl:nil "int64 ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConstantCommand-response)))
  "Returns full string definition for message of type 'ConstantCommand-response"
  (cl:format cl:nil "int64 ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConstantCommand-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConstantCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ConstantCommand-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ConstantCommand)))
  'ConstantCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ConstantCommand)))
  'ConstantCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConstantCommand)))
  "Returns string type for a service object of type '<ConstantCommand>"
  "cs1567p1/ConstantCommand")