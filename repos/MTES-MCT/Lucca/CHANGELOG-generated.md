## Changelog : Lucca (30 derniers jours)

### Résumé
Cette mise à jour apporte des corrections et des améliorations concernant la gestion des données, notamment au niveau des contrôles, des procès-verbaux et des communes. L'application a également été mise à jour avec une nouvelle version (v4.3.9) et des améliorations ont été apportées à la gestion des fichiers CSV lors de la gestion des départements et des communes.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la modification des procès-verbaux (#b001310).
- Amélioration de la gestion des communes et des intercommunalités dans la gestion des départements :
  - Création ou mise à jour des communes et intercommunalités à partir de fichiers CSV.
  - Validation des fichiers CSV uploadés.
  - Amélioration des messages de retour à l'utilisateur lors de l'importation des données (#14d8a4c).
- Ajout du champ `parcelClean` à l'entité `Plot` pour le projet lucca script (#4e41ef5).
- Correction de la relation entre les entités contrôle, procès-verbal, dossier et suppression en cascade pour éviter les erreurs de clé étrangère (#f7bf245).
- Refactorisation des dépôts `Control` et `Minute` pour supprimer le champ `folder` inutile des requêtes (#ba175f7).

### Évolutions techniques
- Mise à jour de la version de l'application à v4.3.7, v4.3.8 et v4.3.9 (#60f3d8b, #8b84707, #82f44bc).
- Ajout du fichier de configuration `config/reference.php` (#09e8bf2).
