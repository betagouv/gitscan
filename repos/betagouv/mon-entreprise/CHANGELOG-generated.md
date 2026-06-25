## Changelog : mon-entreprise (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du comparateur de statuts et des simulateurs, avec une attention particulière portée à l'accessibilité et à la clarté des informations. Des corrections et des améliorations spécifiques ont été apportées pour les cas de Mayotte, et une refonte technique importante a été menée pour préparer le site à l'avenir, notamment avec l'adoption de nouvelles versions de librairies et une meilleure gestion du thème et de l'internationalisation.

### Évolutions fonctionnelles
- **Comparateur de statuts :** Nouvelle mise en page et regroupement des questions pour une meilleure clarté. Ajout d'un bouton pour revenir à la liste des questions et d'un bouton pour réinitialiser les valeurs par défaut.
- **Simulateurs :** Amélioration de l'affichage des avertissements et des objectifs, avec utilisation de tooltips pour plus de concision.
- **Mayotte :** Corrections et ajouts spécifiques pour le calcul des cotisations et des dispenses d'assiette minimale à Mayotte, incluant un avertissement spécifique pour les auto-entrepreneureuses.
- **Cessation d'activité :** Ajout d'un message d'erreur en cas de date de cessation invalide et gestion du changement d'année de simulation.
- **Artiste-auteur :** Mise à jour de la description et du guide IRCEC.
- **Messages :** Les messages sont désormais dismissibles (pouvant être fermés par l'utilisateur).
- **Bandeau Beta :** Le bandeau indiquant que le site est en version beta a été réactivé.

### Évolutions techniques
- **Refonte de l'infrastructure Next.js :** Migration vers React 19 et Storybook 8, amélioration de la gestion du thème (darkMode) via cookies et optimisation de la performance avec Turbopack.
- **Internationalisation :** Refactor de la configuration i18n pour une meilleure gestion du serveur et du client.
- **Suppression de dépendances obsolètes :** Suppression de code et de dépendances inutiles, notamment liées à la gestion des YAML et des cookies.
- **Amélioration du code :** Renommage de fichiers et de fonctions pour une meilleure lisibilité et cohérence. Utilisation de CSS variables pour les fonts.
- **Accessibilité :** Améliorations de l'accessibilité avec l'ajout de rôles ARIA et la correction de contrastes de couleurs.
- **Tests :** Ajout de tests unitaires pour certains composants et hooks.

### Autres changements
- Mise à jour du Smic.
- Mise à jour de la base de données des statistiques (base-stats.json).
- Corrections de typographie et de traductions.
- Amélioration de la documentation et des commentaires.
- Corrections de style et de mise en page.
