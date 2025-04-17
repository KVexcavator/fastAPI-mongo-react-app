import { useLoaderData } from "react-router"
import CarCard from "../components/CarCard"

const Cars = () => {
  const cars = useLoaderData()

  return (
    <div>
      <h1>Available Cars</h1>
      <div className="md:grid md:grid-cols-3 sm:grid sm:grid-cols-2 gap-5">
        {cars.map(car => {
          <CarCard key={car.id} car={car} />
        })}
      </div>
    </div>
  )
}

export default Cars

export const carsLoader = async () => {
  console.log("Back URL: ")
  const res = await fetch(
    `${import.meta.env.VITE_API_URL}/cars/?limit=30`
  )
  const response = await res.json()
  if (!res.ok){
    throw new Error(response.message)
  }
  return response['cars']
}