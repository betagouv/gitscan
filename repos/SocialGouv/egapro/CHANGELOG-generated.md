## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent principalement sur l'amélioration de l'expérience de connexion et de l'authentification, notamment avec l'intégration de Proconnect. Des optimisations de performance ont également été apportées au processus de construction de l'application, et des améliorations ont été faites aux tests et à la configuration du projet.

### Évolutions fonctionnelles
- Amélioration du processus de connexion/déconnexion, avec gestion des sessions et des redirections (#2796).
- Ajout d'une fonctionnalité de déconnexion avant la sélection d'une organisation.
- Ajout d'un environnement de développement Proconnect (#2770).
- Optimisation du temps de construction de l'application via le caching dans le Dockerfile (#2795).
- Restauration des cartes et correction des paramètres de cache invalides (#2776).

### Évolutions techniques
- Ajout de la configuration et de la mise en place de Vitest pour les tests avec DSFR (#2794).
- Nettoyage des fichiers de configuration (#2782).
- Ajout du job `review-auto` à chaque nouvelle branche dans le CI/CD (#2789).
- Correction de l'écrasement des variables d'environnement (#2774).
- Suppression du prompt de sélection d'organisation dans certains cas.
- Tests améliorés pour la répétition des requêtes (#2788).

### Autres changements
- Mise à jour de la version de l'application à 3.15.2 (0b3e634).
- Utilisation des nouvelles informations d'identification Proconnect (040a098).
- Correction de l'URL de test pour l'authentification.
- Correction de l'URL pour les tests avec clean config.
- Ajout de logs pour la déconnexion.
- Ajout d'un test sans clé Keycloak (#2796).
- Correction d'un bug lié à la récupération du siret (#2771).
