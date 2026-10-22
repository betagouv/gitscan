## Changelog : b3desk (30 derniers jours, au 21 octobre 2026)

### Résumé
Cette période a été marquée par l'avancement significatif de l'interface d'administration avec le déploiement du troisième lot de fonctionnalités du Backoffice et la gestion du transfert de propriété des réunions. Des efforts importants ont également été consacrés au renforcement de la sécurité (protection des clés API et jetons) et à la modernisation de la structure du code.

### Évolutions fonctionnelles
- **Administration** : Déploiement du troisième lot de fonctionnalités pour le Backoffice [#375].
- **Gestion des réunions** : Ajout de la fonctionnalité de transfert de propriété des réunions [#391].
- **Expérience utilisateur** : 
    - Amélioration de la gestion des erreurs lors des tentatives de connexion SIP lorsque le service est désactivé.
    - Correction d'erreurs dans la console et sécurisation de l'affichage des noms de réunions et de groupes dans les messages de notification.

### Évolutions techniques
- **Sécurité** : Suppression de l'enregistrement (logging) des clés API Nextcloud et des jetons utilisateurs pour éviter toute fuite de données sensibles.
- **Refactoring** : Suppression du code JavaScript embarqué pour améliorer la structure et la maintenabilité du projet [#439].
- **Infrastructure et CI/CD** : 
    - Correction de la chaîne d'intégration continue (CI).
    - Mise à jour des exigences de version Python (fin du support des versions antérieures à 3.14).
- **Tests** : Amélioration de la fiabilité de la suite de tests (correction de tests cassés et mise à jour de `pytest-iam`).

### Autres changements
- Mises à jour diverses des dépendances du projet.
