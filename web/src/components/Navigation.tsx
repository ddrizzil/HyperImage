'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Search, Menu, X } from 'lucide-react'
import { useState } from 'react'
import { cn } from '@/lib/utils'

export function Navigation() {
  const pathname = usePathname()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const navLinks = [
    { href: '/', label: 'Home' },
    { href: '/techniques', label: 'Imaging Techniques' },
    { href: '/rf-techniques', label: 'RF Techniques' },
    { href: '/optics', label: 'Optics Reference' },
    { href: '/pages', label: 'Pigments & Chemistry' },
    { href: '/multimodal', label: 'Multimodal' },
    { href: '/ml', label: 'Machine Learning' },
  ]

  return (
    <nav className="sticky top-0 z-50 bg-primary-800 text-white shadow-lg">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <span className="text-xl font-bold">HyperImage</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex md:items-center md:space-x-6">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className={cn(
                  'px-3 py-2 text-sm font-medium transition-colors hover:bg-primary-700 rounded-md',
                  pathname === link.href && 'bg-primary-700'
                )}
              >
                {link.label}
              </Link>
            ))}
          </div>

          {/* Search Button */}
          <Link
            href="/techniques?search=true"
            className="hidden md:flex items-center space-x-2 px-4 py-2 bg-primary-700 hover:bg-primary-600 rounded-md transition-colors"
          >
            <Search className="h-4 w-4" />
            <span className="text-sm">Search</span>
          </Link>

          {/* Mobile menu button */}
          <button
            type="button"
            className="md:hidden p-2 rounded-md hover:bg-primary-700"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle menu"
          >
            {mobileMenuOpen ? (
              <X className="h-6 w-6" />
            ) : (
              <Menu className="h-6 w-6" />
            )}
          </button>
        </div>

        {/* Mobile menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 space-y-2">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className={cn(
                  'block px-3 py-2 rounded-md text-sm font-medium hover:bg-primary-700',
                  pathname === link.href && 'bg-primary-700'
                )}
                onClick={() => setMobileMenuOpen(false)}
              >
                {link.label}
              </Link>
            ))}
            <Link
              href="/techniques?search=true"
              className="flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium hover:bg-primary-700"
              onClick={() => setMobileMenuOpen(false)}
            >
              <Search className="h-4 w-4" />
              <span>Search</span>
            </Link>
          </div>
        )}
      </div>
    </nav>
  )
}

