import QtQuick 2.15
import QtQuick.Controls 2.15

import QtGraphicalEffects 1.15


Item {

    property color btnColorDefault: "#000000"
    property color btnColorMouseOver: "#8c0909"
    property color btnColorClicked: "#d10808"

    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("Remove Faces")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 10
            font.pointSize: 16
        }

        Label {
            id: label1
            color: "#ffffff"
            text: qsTr("No Face Found")
            anchors.verticalCenter: parent.verticalCenter
            font.pointSize: 18
            anchors.horizontalCenter: parent.horizontalCenter
            visible: false
        }

        Rectangle {
            id: rectangle1
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: label.bottom
            anchors.bottom: parent.bottom
            clip: true
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 0
            anchors.topMargin: 10
            visible: true

            Rectangle {
                id: rectangle2
                width: 300
                height: 200
                color: "#00000000"
                Image {
                    id: image
                    anchors.fill: parent
                    source: ""
                    fillMode: Image.PreserveAspectFit

                    Button {
                        id: button
                        anchors.fill: parent
                        flat: true

                        QtObject{
                            id: internal

                            // Mouse Hover and Click Change Color
                            property var dynamicColor: if(button.down){
                                                           button.down ? btnColorClicked : btnColorDefault
                                                       } else {
                                                           button.hovered ? btnColorMouseOver : btnColorDefault
                                                       }
                        }

                        background: Rectangle{
                            id: bgBtn
                            color: "#00000000"
                            radius: 10
                        }

                        Image {
                            id: image1
                            width: 50
                            height: 50
                            anchors.verticalCenter: parent.verticalCenter
                            source: "../../images/svg_images/trash_icon.svg"
                            anchors.horizontalCenter: parent.horizontalCenter
                            fillMode: Image.PreserveAspectFit
                            visible: true
                            antialiasing: true
                        }

                        ColorOverlay{
                            anchors.fill: image1
                            source: image1
                            color: internal.dynamicColor
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.horizontalCenter: parent.horizontalCenter
                            antialiasing: true
                            width: 50
                            height: 50
                        }
                        onClicked: {
                            removeBackend.deleteImage()
                        }
                    }
                }
            }

        }
    }

    Connections{
        target: removeBackend

        function onRemoveImage(value) {
            if (value === "true") {
                rectangle1.visible = false
                label1.visible = true
            }
            else {
                rectangle1.visible = true
//                label1.visible = false
            }
        }
    }

    Connections{
        target: backend
        function onRemoveImage(value) {
            if (value === "true") {
                rectangle1.visible = false
                label1.visible = true
            }
            else {
                rectangle1.visible = true
            }
        }
        function onSetImagePath(value){
            image.source = value
//            print("path ", value)
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:5}
}
##^##*/
