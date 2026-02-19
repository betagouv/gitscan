## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent principalement sur l'amélioration de l'expérience de connexion et de l'authentification, ainsi que sur l'optimisation des performances et de la configuration de l'application, notamment en préparation de l'environnement de développement Proconnect. Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration du processus de connexion et de déconnexion, avec gestion des sessions et des redirections (#2796).
- Ajout d'une fonctionnalité de déconnexion avant la sélection d'une organisation.
- Correction d'un bug empêchant l'affichage correct du code NAF et d'autres informations non diffusibles (#2739, #2776).
- Ajout d'un texte explicatif pour le bouton "plus d'informations".

### Évolutions techniques
- Optimisation du temps de build Docker grâce à l'utilisation du caching (#2795).
- Ajout de la configuration et de la mise en place de Vitest pour les tests avec DSFR (#2794).
- Nettoyage des fichiers de configuration (#2782).
- Ajout du job `review-auto` à chaque nouvelle branche pour l'automatisation des revues de code (#2789).
- Amélioration de la vitesse de build de l'application (#2771).
- Correction de problèmes liés aux variables d'environnement Proconnect.
- Mise à jour des credentials Proconnect.

### Autres changements
- Restauration des maps et correction des paramètres de cache invalides (#2776).
- Correction d'un problème de non-diffusibilité en production (#2774).
- Publication des versions 3.15.2 et 3.15.1 avec des corrections de bugs.
- Suppression de l'utilisation d'une clé Keycloak pour les tests (#2796).
- Correction de tests E2E pour la requête REPEQ (#2788).
- Ajout d'un environnement de développement Proconnect (#2770).
