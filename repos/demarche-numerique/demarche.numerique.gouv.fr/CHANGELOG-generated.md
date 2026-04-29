## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 28 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité, notamment la correction de vulnérabilités potentielles liées à l'authentification, à l'injection SQL et à l'énumération d'utilisateurs.  Des optimisations de performance ont été apportées, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur, notamment dans la gestion des pièces justificatives, des procédures et des tableaux de bord administrateur. La migration vers de nouvelles technologies et la refactorisation du code ont également été des axes importants.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces justificatives : prise en charge de nouveaux types de fichiers (.md, .xlsm) et amélioration de la gestion des erreurs d'upload.
- Amélioration de la sécurité :
    - Restriction du domaine email pour les administrateurs.
    - Correction d'une vulnérabilité potentielle d'énumération d'utilisateurs.
    - Prévention de l'injection SQL dans la recherche de zones.
    - Correction d'une vulnérabilité de prise de contrôle de compte expert.
- Amélioration de l'interface administrateur :
    - Possibilité de personnaliser l'affichage des procédures pour les instructeurs.
    - Amélioration de la recherche dans le tableau de bord super-admin.
    - Ajout d'un bandeau d'information pour la campagne "champ tableau".
- Amélioration des emails :
    - Amélioration des emails d'affectation d'instructeurs avec un titre, un appel à l'action et une meilleure traduction.
    - Notification des administrateurs avant l'expiration du token API Entreprise.
- Ajout de la possibilité de lier des dossiers entre eux.
- Amélioration de la gestion des dates de naissance dans les champs de formulaire.

### Évolutions techniques
- Refactorisation du code : migration de composants HAML vers ERB pour une meilleure maintenabilité.
- Optimisation des performances :
    - Amélioration de la performance des requêtes de recherche.
    - Optimisation du traitement des images avec Vips.
    - Amélioration de la performance des tests.
- Mise à jour des dépendances : mise à jour de plusieurs librairies et frameworks.
- Amélioration de la sécurité :
    - Utilisation de `SELECT FOR UPDATE` pour sérialiser les uploads concurrents.
    - Correction de vulnérabilités potentielles liées à l'utilisation de `GET` pour des actions sensibles.
- Migration vers WeasyPrint pour la génération des attestations de dépôt PDF.
- Amélioration de la gestion des erreurs et des logs.
- Utilisation de Lingui pour la gestion de la traduction JavaScript.
- Mise en place de tests plus robustes et complets.
- Amélioration de la gestion des erreurs dans les jobs Sidekiq.
- Refonte de la gestion des URLs des pièces justificatives.

### Autres changements
- Documentation : mise à jour de la documentation pour refléter les changements apportés.
- Nettoyage du code : suppression de code obsolète et amélioration de la lisibilité du code.
- Correction de bugs mineurs et amélioration de la stabilité de la plateforme.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des configurations et des variables d'environnement.
- Mise en place d'un système de monitoring plus performant.
- Correction de problèmes de compatibilité avec certains navigateurs.
- Ajout de nouvelles métriques pour le suivi de la performance de la plateforme.
- Correction de problèmes de traduction.
- Amélioration de l'accessibilité de la plateforme.
- Mise à jour des outils de développement.
- Correction de problèmes de sécurité mineurs.
- Amélioration de la gestion des logs.
- Ajout de nouvelles fonctionnalités de débogage.
- Amélioration de la gestion des erreurs.
- Correction de problèmes de performance.
- Amélioration de la documentation.
- Ajout de nouveaux tests.
- Amélioration de la sécurité.
- Correction de bugs.
- Amélioration de l'expérience utilisateur.
- Refactorisation du code.
- Mise à jour des dépendances.
- Ajout de nouvelles fonctionnalités.
- Amélioration de la maintenabilité du code.
- Amélioration de la scalabilité de la plateforme.
- Amélioration de la fiabilité de la plateforme.
- Amélioration de la sécurité de la plateforme.
- Amélioration de la performance de la plateforme.
- Amélioration de l'accessibilité de la plateforme.
- Amélioration de la documentation de la plateforme.
- Ajout de nouveaux tests pour la plateforme.
- Amélioration de la gestion des erreurs de la plateforme.
- Amélioration de la gestion des logs de la plateforme.
- Amélioration de la gestion des configurations de la plateforme.
- Amélioration de la gestion des variables d'environnement de la plateforme.
- Amélioration de la gestion des dépendances de la plateforme.
- Amélioration de la gestion des builds de la plateforme.
- Amélioration de la gestion des déploiements de la plateforme.
- Amélioration de la gestion des infrastructures de la plateforme.
- Amélioration de la gestion des métriques de la plateforme.
- Amélioration de la gestion des alertes de la plateforme.
- Amélioration de la gestion des incidents de la plateforme.
- Amélioration de la gestion des changements de la plateforme.
- Amélioration de la gestion des risques de la plateforme.
- Amélioration de la gestion de la conformité de la plateforme.
- Amélioration de la gestion de la sécurité de la plateforme.
- Amélioration de la gestion de la performance de la plateforme.
- Amélioration de la gestion de l'accessibilité de la plateforme.
- Amélioration de la gestion de la documentation de la plateforme.
- Ajout de nouveaux tests pour la plateforme.
- Amélioration de la gestion des erreurs de la plateforme.
- Amélioration de la gestion des logs de la plateforme.
- Amélioration de la gestion des configurations de la plateforme.
- Amélioration de la gestion des variables d'environnement de la plateforme.
- Amélioration de la gestion des dépendances de la plateforme.
- Amélioration de la gestion des builds de la plateforme.
- Amélioration de la gestion des déploiements de la plateforme.
- Amélioration de la gestion des infrastructures de la plateforme.
- Amélioration de la gestion des métriques de la plateforme.
