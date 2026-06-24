## Changelog : envergo (30 derniers jours, au 23 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la performance et de la stabilité de l'application, notamment au niveau de la gestion des données et des requêtes. Des corrections de bugs et des ajustements ont été apportés pour améliorer l'expérience utilisateur, en particulier concernant la gestion des critères Natura 2000, des données ICPE et des alertes. L'interface utilisateur a également été affinée et des nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des données et des configurations.

### Évolutions fonctionnelles
- Ajout de la gestion des cartes de densité sur la page de configuration.
- Implémentation d'une procédure d'urgence avec un formulaire dédié et une alerte d'information.
- Amélioration de l'affichage et de la gestion des critères Natura 2000, incluant la prise en compte des haies et des zones spécifiques.
- Correction d'un bug empêchant la soumission des ICPE non soumis et sans dépôt LSE.
- Ajout de la possibilité d'importer plusieurs fichiers.
- Amélioration de la gestion des actions à entreprendre pour les ICPE, avec des modèles spécifiques pour les cas par cas.
- Modification du libellé "Administration" par "Espace instruction" pour plus de clarté.
- Ajout de la possibilité d'importer des données Taxref pour mettre à jour les espèces.
- Amélioration de l'affichage des données dans les tableaux, notamment l'ajout d'unités.
- Correction de l'affichage des données dans les emails d'avis.
- Amélioration de la gestion des conditions de plantation.

### Évolutions techniques
- Optimisation des performances de l'application, notamment au niveau des requêtes en base de données et de la récupération des données.
- Refactorisation du code pour améliorer la qualité et la maintenabilité.
- Mise à jour des dépendances, incluant Playwright et Node.js.
- Amélioration de la sécurité en whitelistant les URL mappings vers les domaines locaux.
- Suppression de données sensibles dans les URL.
- Correction de bugs et amélioration des tests unitaires et d'intégration.
- Mise en place de tests plus complets pour les critères ICPE.
- Amélioration de la gestion des migrations de base de données.
- Correction de conflits de migration.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.

### Autres changements
- Correction de fautes de frappe et amélioration de la qualité du code.
- Mise à jour de la documentation.
- Suppression de code inutile.
- Amélioration des messages d'erreur.
- Ajout de tests pour les nouvelles fonctionnalités.
- Correction de problèmes de synchronisation entre les templates HTML et texte des avis.
- Suppression du modèle `RecipientStatus` et des fonctionnalités associées à Brevo pour la gestion du RGPD.
- Suppression du suivi des événements Brevo.
- Correction de problèmes liés à la gestion des conditions et des coefficients pour les RU (Réglementation Urbanisme).
- Amélioration de la gestion des erreurs et des exceptions.
