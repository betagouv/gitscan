## Changelog : france-chaleur-urbaine (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la page de simulation et le formulaire de contact. Des corrections de bugs et des optimisations ont été apportées, ainsi que des mises à jour des données réseaux de chaleur et de la gestion des fichiers pour les contributions. L'intégration de PostHog pour le suivi analytique permet une meilleure compréhension du comportement des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une page de méthodologie expliquant le fonctionnement du simulateur.
- Amélioration de l'affichage et de la gestion des erreurs sur la page de résultat du simulateur, notamment en mode mobile.
- Ajout d'un bouton retour sur la page de méthodologie.
- Simplification du processus de copie de la simulation.
- Suppression du bouton "Je Donne Mon Avis" remplacé par un sondage PostHog.
- Ajout d'un formulaire de contact remplaçant l'adresse email.
- Amélioration du suivi des événements avec PostHog pour une meilleure analyse de l'utilisation du site.
- Ajout d'un CTA pour les utilisateurs non raccordables.
- Possibilité de filtrer les fichiers géographiques (shapefile et PDF) pour les contributions.
- Affichage des réseaux de chaleur non ouverts en gris sur la carte.
- Ajout de nouveaux modes de chauffage (Pac géo maison et Chaudière biomasse maison) dans le simulateur.
- Amélioration de l'affichage du gain DPE et du bouton "Comparer les solutions" en mode mobile.

### Évolutions techniques
- Refactorisation de l'appel à l'API `location-infos` avec trpc pour plus d'efficacité.
- Utilisation de trpc pour l'appel à Airtable.
- Transformation de l'appel RNB en trpc.
- Création de modules pour factoriser le code et améliorer la maintenabilité (chaleur-renouvelable, opendata).
- Mise à jour de la version de Publicodes.
- Suppression du markdown dans certains composants et remplacement par du HTML.
- Ajout de scripts pour la gestion et l'import des données Batenr et des données réseaux de chaleur.
- Intégration de PostHog pour le suivi analytique.
- Amélioration de la gestion des types et des paramètres par défaut.
- Suppression de fichiers et de code inutilisés.
- Mise à jour des données réseaux de chaleur avec les DLE 2024.

### Autres changements
- Ajout de documentation sur l'utilisation de Publicodes et le lancement du serveur.
- Ajout de fichiers `.editorconfig` pour améliorer la cohérence du code.
- Mise à jour des statistiques mensuelles.
- Amélioration des commentaires et de la documentation.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout de tests pour vérifier l'adresse.
- Suppression de la bannière du comparateur de coûts.
