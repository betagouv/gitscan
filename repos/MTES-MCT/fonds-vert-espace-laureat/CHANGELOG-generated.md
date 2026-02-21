## Changelog : fonds-vert-espace-laureat (30 derniers jours)

### Résumé
Cette mise à jour apporte des corrections concernant la gestion des données provenant de Grist, notamment le traitement des champs d'action manquants. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le pré-remplissage correct des données lorsque le champ "action" de l'API Grist est vide. (#247aa3b)

### Évolutions techniques
- Ajout de logs pour les enregistrements Grist avec un champ d'action invalide, facilitant le débogage et l'identification des problèmes de données. (#24941b1)
- Mise à jour des dépendances du projet. (#ed4a59f, #009c029)
