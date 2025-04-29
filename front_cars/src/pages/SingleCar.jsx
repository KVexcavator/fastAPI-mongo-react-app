import { useLoaderData } from "react-router"
import CarCard from "../components/CarCard"

const SingleCar = () => {
  const car = useLoaderData()
  
  return (
    <CarCard car={car} />
  )
}

export default SingleCar