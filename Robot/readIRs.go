package main

import(
	"fmt"

	"/src/github.com/hybridgroup/gobot"
	"/src/github.com/hybridgroup/gobot/platforms/firmata"
	"/src/github.com/hybridgroup/gobot/platforms/gpio"
)

func main(){
	gbot := gobot.NewGobot()
	firmataAdaptor := firmata.NewFirmataAdaptor("firmata","/dev/ttyACM0")
	sensor0 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor0","0")
	sensor1 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor1","1")
	sensor2 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor2","2")
	sensor3 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor3","3")
	sensor4 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor4","4")
	sensor5 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor5","5")
	sensor6 := gpio.NewAnalogSensorDrive(firmataAdaptor,"sensor6","6")

	work := func(){
		fmt.Println("sensor0",sensor0)
		fmt.Println("sensor1",sensor1)
		fmt.Println("sensor3",sensor3)
		fmt.Println("sensor4",sensor4)
		fmt.Println("sensor5",sensor5)
		fmt.Println("sensor6",sensor6)
	}



	robot := gobot.NewRobot("sensorBot",
		[]gobot.Connection{firmataAdaptor},
		[]gobot.Device{sensor0, sensor1, sensor2, sensor3, sensor4, sensor5, sensor6},
		work,
	)

	gbot.AddRobot(robot)

	gbot.Start()

}
