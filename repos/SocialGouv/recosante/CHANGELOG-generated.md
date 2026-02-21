## Changelog : recosante (30 derniers jours)

### Résumé
Cette mise à jour apporte une nouvelle fonctionnalité permettant aux utilisateurs de signaler la fin du service, ainsi qu'une migration importante des recommandations vers un nouveau format de fichier. Plusieurs corrections de bugs et améliorations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une bannière de fin de service pour informer les utilisateurs. (#678)
- Possibilité d'ajouter des villes et des indices à ses favoris. (#666)
- Correction de bugs concernant l'affichage de certaines pages et la gestion des erreurs. (#668)

### Évolutions techniques
- Migration des recommandations de Google Sheets vers un fichier plus adapté. (#675)
- Refactorisation des schémas utilisateur pour améliorer le traitement des données. (#674)
- Refactorisation des contrôleurs d'utilisateur pour utiliser des schémas plus performants. (#667)
- Amélioration de la configuration du CI/CD avec l'utilisation de buildkit. (#655)
- Augmentation des ressources CPU allouées à l'API. (#1fc6f17)

### Autres changements
- Correction d'une faute de frappe dans la configuration du sous-domaine. (#2a164ae)
- Ajout d'une vérification de l'existence des notifications. (#650)
