## Changelog : flask-storage (30 derniers jours, au 16 juin 2026)

### Résumé
Les récentes mises à jour de flask-storage se concentrent sur la correction de bugs liés au backend S3. Ces corrections améliorent la précision de la suppression de fichiers et garantissent que le type de contenu des fichiers est correctement identifié lors du chargement.

### Évolutions fonctionnelles
- Correction d'un bug dans le backend S3 où la suppression de fichiers ne supprimait pas uniquement le fichier ciblé, mais tous les fichiers partageant le même préfixe de clé [#19](https://github.com/etalab/flask-storage/pull/19).
- Amélioration de la gestion du type de contenu (MIME type) lors du chargement de fichiers sur S3, en corrigeant un problème où le type de contenu n'était pas toujours correctement deviné [#18](https://github.com/etalab/flask-storage/pull/18).

### Évolutions techniques
Aucune évolution technique majeure n'a été apportée durant cette période.

### Autres changements
Aucun autre changement significatif à signaler.
