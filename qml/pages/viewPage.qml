import QtQuick 2.15
import QtQuick.Controls 2.15
import '../controls'

Item {
    property int n: 100
    Rectangle {
        id: rectangle
        color: "#16181d"
        anchors.fill: parent

        Label {
            id: label
            color: "#ffffff"
            text: qsTr("Faces")
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

            Image {
                id: image
//                visible: false
                x: 8
                y: 0
                width: 250
                source: "../../images/captured/img_1.jpg"
                fillMode: Image.PreserveAspectFit
            }

//            ScrollView {
//                id: scrollView
//                anchors.fill: parent

//                Grid {
//                    id: grid
//                    anchors.fill: parent
//                    columns: 5
//                    clip: true
//                    flow: Grid.LeftToRight
//                    spacing: 10

//                    Repeater {
//                        id: repeater
//                        width: rectangle1.width
//                        anchors.fill: parent
//                        clip: true
//                        model: 100
//                        Image {
//                            id: image
//                            width: 150
//                            height: 150
//                            source: "../../images/faces/"+index+".jpg"
//                            fillMode: Image.PreserveAspectFit

//                            Button {
//                                id: button
//                                visible: false
//                                text: qsTr("Button")
//                            }
//                        }

//                    }


//                }
//            }

        }
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:680}
}
##^##*/
