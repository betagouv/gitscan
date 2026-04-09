## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en intégrant une fonctionnalité de médiathèque pour les préconisations, en optimisant les performances des requêtes de données et en améliorant le formulaire de feedback avec l'envoi d'emails directement depuis la préproduction. Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser et sécuriser la plateforme.

### Évolutions fonctionnelles
- Ajout d'une médiathèque pour les préconisations, permettant de gérer et d'afficher des contenus enrichis (images, textes formatés) dans les recommandations. [#56](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/56)
- Intégration de données scolaires (écoles) pour affiner l'analyse et les préconisations. [#57](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/57)
- Mise en place d'un formulaire de feedback avec envoi d'emails directement depuis l'environnement de préproduction. [#51](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/51)
- Ajout de liens "Donner mon avis" et "Contact" pour faciliter la communication avec les utilisateurs.
- Amélioration de la présentation des recommandations avec l'ajout de points clés ("keyPoints") et d'une section "à retenir".
- Ajout d'un compteur d'envois d'emails de diagnostic pour suivi.
- Ajout d'un lien vers les engagements de service.
- Amélioration de la recherche avec une barre de recherche et un état vide géré.

### Évolutions techniques
- Optimisation des requêtes de données, notamment pour l'affichage des données OSM et des nuisances sonores, afin d'améliorer les performances.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité, notamment en découpant les composants et en supprimant le code inutilisé.
- Mise en place d'une configuration Biome pour le linting et le formatage du code.
- Migration vers un nouveau contrôleur d'envoi d'emails en Node.js, remplaçant l'ancien contrôleur Python.
- Amélioration de la sécurité en ajoutant une limitation du taux d'envoi d'emails pour éviter le spam.
- Correction de vulnérabilités potentielles (CVE) et renforcement de la sécurité des URLs.
- Mise à jour des pipelines CI/CD pour l'automatisation des déploiements.
- Utilisation de slugs pour les données, améliorant l'URL et l'accessibilité.
- Correction de problèmes liés aux index géométriques dans la base de données.

### Autres changements
- Mise à jour de la documentation.
- Corrections de typographie et d'erreurs de wording.
- Amélioration de l'accessibilité (a11y) de certains composants.
- Ajout de logs pour faciliter le débogage et le suivi des performances.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de variables d'environnement pour la configuration de l'application.
- Suppression de collections Strapi inutilisées.
- Amélioration des noms de composants pour plus de clarté.
