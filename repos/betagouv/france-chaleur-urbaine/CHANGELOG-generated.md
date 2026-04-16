## Changelog : france-chaleur-urbaine (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page d'accueil et le simulateur simplifié, avec l'ajout de nouveaux contenus et une refonte de l'affichage. Des améliorations techniques ont également été apportées pour optimiser la gestion des données, les tests et la configuration des emails. L'administration a été enrichie avec de nouvelles fonctionnalités pour la gestion des utilisateurs et des demandes en masse.

### Évolutions fonctionnelles
- **Simulateur simplifié :** Refonte complète de la landing page avec de nouveaux visuels, des témoignages et un carrousel d'articles. Amélioration du CTA et du tracking.
- **Page "Qui sommes-nous" :** Mise à jour des textes et du contenu.
- **Gestion des réseaux de chaleur :** Ajout de colonnes (et donc de filtres) dans la liste des réseaux de chaleur/froid/en construction (notamment pour l'affichage de l'écoréseau).
- **Modal contact réseau de chaleur :** Ajout d'un événement de partage par email.
- **Formulaire de contact :** Possibilité de ne pas renseigner le contact lors de la création de demandes en masse.
- **Admin :**
    - Ajout de la possibilité de créer des demandes en masse pour un utilisateur.
    - Amélioration de l'affichage des événements dans l'interface d'administration.
    - Correction du filtre "Gestionnaires".
    - Affichage du type de structure dans l'admin.
    - Correction de la sauvegarde de l'adresse lors de la vérification d'éligibilité.
- **Affichage général :** Ajout d'icônes à côté des titres des cartes.
- **Emails :** Envoi des emails depuis une adresse no-reply beta.gouv. Amélioration du style et de l'harmonisation des templates.

### Évolutions techniques
- **Dépendances :** Mise à jour des dépendances du projet.
- **Tests :** Correction de tests suite à des modifications et ajout de tests pour la gestion des adresses.
- **Infrastructure :** Configuration de l'envoi d'emails en local.
- **Code :**
    - Refactorisation du code des iframes pour une meilleure maintenabilité.
    - Amélioration du typage de certaines variables et composants.
    - Suppression de code inutile et amélioration de la lisibilité du code.
    - Utilisation de classes Tailwind CSS canoniques.
    - Factorisation de structures de données pour le formulaire de contact.
- **Images :** Conversion des images en format WebP pour optimiser les performances.

### Autres changements
- **Documentation :** Mise à jour de la note méthodologique du comparateur.
- **Configuration :** Ajout de fichiers ignorés par Git pour la configuration locale.
- **Tracking :** Amélioration du nommage du tracking pour le simulateur simplifié et ajout d'événements PostHog pour le partage de simulation.
- **Écoréseaux :** Ajout d'un script d'import des écoréseaux et des données correspondantes.
