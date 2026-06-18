## Changelog : approbiom (30 derniers jours, au 16 juin 2026)

### Résumé
Le projet approbiom a connu un développement rapide au cours des 30 derniers jours, passant d'un dépôt initialisé à une base solide pour la création de widgets personnalisés pour Grist. L'accent a été mis sur la construction de widgets interactifs, notamment des tableaux, des barres de recherche, des sélecteurs et une carte interactive, avec une attention particulière à l'intégration de l'esthétique DSFR et à la configuration des widgets via l'interface de Grist. L'infrastructure de build et de déploiement a également été mise en place.

### Évolutions fonctionnelles
- Ajout d'un widget de tableau avec possibilité de choisir les colonnes à afficher et leur ordre d'affichage. [#10](https://github.com/betagouv/approbiom/issues/10)
- Implémentation d'une barre de recherche avec filtre par tags. [#13](https://github.com/betagouv/approbiom/issues/13)
- Création d'un sélecteur unique et multiple pour l'édition de cellules. [#12](https://github.com/betagouv/approbiom/issues/12)
- Ajout d'un widget de carte interactive affichant les départements. [#8](https://github.com/betagouv/approbiom/issues/8)
- Possibilité de configurer les libellés des sélecteurs et de la barre de recherche depuis l'interface de configuration de Grist.
- Ajout d'un total pour les colonnes de type entier dans le sélecteur de tableau.
- Amélioration de l'affichage des valeurs par défaut dans les sélecteurs d'édition.
- Ajout de barres de défilement au sélecteur de tableau pour une meilleure lisibilité.
- Ajout d'un titre configurable au widget tableau.
- Ajout d'une liste déroulante personnalisable.

### Évolutions techniques
- Mise en place d'une infrastructure de build avec Vite pour la création de widgets multi-pages.
- Configuration d'un workflow CI/CD avec GitHub Actions pour la construction et le déploiement sur GitHub Pages.
- Utilisation des types Grist Plugin API pour une meilleure intégration avec la plateforme.
- Intégration de l'esthétique DSFR pour les widgets.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Initialisation de tests E2E avec Playwright pour le widget carte.

### Autres changements
- Amélioration de l'expérience de développement avec la configuration d'un environnement de développement local avec Grist.
- Suppression de fichiers et dossiers inutiles.
- Correction de problèmes de linting.
- Ajout d'un fichier `.nojekyll` pour éviter les problèmes de déploiement sur GitHub Pages.
- Initialisation du projet et premiers commits.
