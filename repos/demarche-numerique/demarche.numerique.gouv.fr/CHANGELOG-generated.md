## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 7 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de sécurité significatives, notamment concernant la gestion des accès, la validation des données et la protection contre les attaques potentielles. Des optimisations de performance ont également été apportées, en particulier au niveau de la gestion des données géographiques et du traitement des fichiers. Enfin, plusieurs corrections de bugs et des améliorations de l'expérience utilisateur ont été implémentées.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces justificatives, notamment en permettant l'upload de fichiers `.md` et `.xlsm` [#13007](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13007).
- Possibilité pour les administrateurs de personnaliser les tableaux des dossiers pour les instructeurs [#12798](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12798).
- Ajout d'un titre "sticky" sur les pages d'administration pour une meilleure navigation [#12961](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12961).
- Amélioration de l'affichage des informations liées aux dossiers liés (suppression, expiration) [#12932](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12932).
- Amélioration de la gestion des notifications et des alertes, notamment pour les experts et les administrateurs.
- Possibilité de lier un dossier existant lors de la création d'une nouvelle demande.

### Évolutions techniques
- Migration des jobs de longue durée vers Sidekiq pour une meilleure gestion des tâches asynchrones et une meilleure résilience [#13093](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13093), [#13102](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13102).
- Optimisation des performances de l'API géographique grâce à la mise en cache des données [#13099](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/13099).
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles (IDOR, injection SQL, etc.) [#12986](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12986), [#12984](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/issues/12984).
- Mise à jour des dépendances et des librairies utilisées.
- Utilisation de Vips pour le traitement des images afin d'améliorer les performances et la qualité.
- Suppression de code obsolète (SAML).
- Amélioration du système de gestion des erreurs et des logs.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et amélioration de l'expérience utilisateur.
- Amélioration des tests unitaires et d'intégration.
- Refactorisation de composants HAML vers ERB.
- Ajout de commentaires et de documentation au code.
- Correction de problèmes de performance liés à la gestion des adresses géographiques.
- Amélioration de la gestion des erreurs lors du traitement des fichiers.
- Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- Correction de problèmes de sécurité liés à l'upload de fichiers.
- Amélioration de la gestion des emails et des notifications.
- Correction de problèmes d'affichage et de mise en page.
- Suppression de code mort et simplification du code existant.
- Amélioration de la gestion des configurations et des variables d'environnement.
- Ajout de nouvelles métriques et de monitoring pour suivre les performances de l'application.
