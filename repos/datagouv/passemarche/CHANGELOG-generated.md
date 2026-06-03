## Changelog : passemarche (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Passe Marché se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des lots et l'accès aux candidatures. Des corrections et des refactorings techniques ont également été réalisés pour améliorer la stabilité et la maintenabilité de l'application.

### Évolutions fonctionnelles
- **Gestion des lots :** Refonte de la page de sélection des lots avec une présentation en deux états (sélectionner / préparer). Affichage des types de lots reçus de la plateforme d'achat.
- **Tableau de bord candidat :**
    - Ajout d'une bannière informant des candidatures en cours.
    - Pagination des candidatures affichées.
    - Affichage du nom de l'acheteur pour chaque candidature.
    - Possibilité de consulter une candidature spécifique.
    - Ajout d'un lien pour accéder à la page de consultation d'une candidature.
- **Attestations candidat :** Amélioration de l'affichage des annexes pour les candidatures multi-lots.
- **URLs de retour :** Configuration des URLs de retour pour l'acheteur et le candidat après authentification.
- **Suppression de candidature :** Ajout de la fonctionnalité permettant de supprimer une candidature.

### Évolutions techniques
- **Refactoring de l'authentification candidat :** Simplification et amélioration de la gestion de l'authentification des candidats.
- **Unification des presenters :** Regroupement des méthodes communes des presenters pour une meilleure cohérence et maintenabilité.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment :
    - `puma` (8.0.1 -> 8.0.2)
    - `rubyzip` (3.3.0 -> 3.3.1)
    - `jbuilder` (2.15.0 -> 2.15.1)
    - `doorkeeper` (5.9.0 -> 5.9.1)
    - `solid_cable` (3.0.12 -> 4.0.0)
    - `view_component` (4.8.0 -> 4.11.0)
    - `bootsnap` (1.24.0 -> 1.24.5)
    - `pagy` (43.5.3 -> 43.5.5)
    - `devise` (5.0.3 -> 5.0.4)
    - `selenium-webdriver` (4.43.0 -> 4.44.0)
    - `faraday` (2.14.1 -> 2.14.2)
    - `thruster` (0.1.20 -> 0.1.21)

### Autres changements
- Ajout de tests Cucumber pour les pages de synchronisation et le tableau de bord candidat.
- Amélioration de la documentation et des traductions.
- Corrections de bugs et améliorations de la qualité du code.
- Ajout de la colonne `buyer_name` à la table `public_markets`.
- Récupération du nom de l'acheteur (raison sociale) depuis l'INSEE après la création d'un marché.
