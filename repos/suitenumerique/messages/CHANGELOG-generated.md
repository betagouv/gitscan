## Changelog : messages (30 derniers jours)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'importation et l'exportation de boîtes aux lettres, notamment la prise en charge de formats comme PST et MBOX. L'interface utilisateur a également été améliorée avec de nouvelles fonctionnalités pour l'éditeur de signature et de messages, ainsi que des optimisations de performance et de sécurité. Des correctifs ont été apportés pour résoudre des problèmes liés à l'importation de fichiers volumineux, la gestion des pièces jointes et la sécurité XSS.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter une boîte aux lettres au format MBOX avec les labels (#553).
- Prise en charge de l'importation de fichiers PST (#544).
- Ajout d'une liste noire pour les préfixes de boîtes de réception personnelles (#540).
- Amélioration de l'éditeur de signature avec une disposition en plusieurs colonnes (#551).
- Ajout d'un bouton "Imprimer" dans le menu contextuel des messages (#518).
- Possibilité d'ajouter des images directement dans le corps des messages via l'éditeur BlockNote (#511, #81db181).
- Ajout d'une vue "Intégrations" dans les paramètres de la boîte aux lettres (#488).
- Possibilité de transférer les pièces jointes lors du renvoi d'un message (#485).
- Ajout d'une action de nouvelle tentative d'envoi dans l'admin Django et d'un filtre par statut de livraison (#499).
- Amélioration de la gestion des invitations de calendrier (#481).
- Ajout d'un dossier "Sortie" conditionnel (#522).

### Évolutions techniques
- Mise à niveau des étapes du workflow GitHub Actions (#555).
- Ajout du support de la plateforme ARM64 pour les builds d'images Docker (#554).
- Utilisation d'un webhook et de la journalisation au lieu de Pushgateway pour les auto-vérifications MDA (#550).
- Activation des événements de tâches Celery pour la surveillance des workers (#549).
- Optimisation de la sérialisation de MessageTemplate et de la gestion du corps (#545).
- Mise à niveau de django-lasuite de 0.0.19 à 0.0.24 (#546).
- Renforcement des contrôles DNS et ajout d'enregistrements configurables (#522).
- Refactorisation de certains codes de permissions pour les viewsets (#503).
- Amélioration du routage des tâches sur les queues Celery (#504).
- Utilisation du cache Redis pour le développement (#515).

### Autres changements
- Amélioration de la formulation dans la boîte de réception (#539).
- Ajout de métriques d'utilisation du stockage avec une nouvelle route API (#538).
- Correction de bugs liés à l'importation de fichiers MBOX volumineux (#516).
- Correction de problèmes liés à la duplication de la création de destinataires (#496).
- Correction d'erreurs SSL et amélioration de la gestion des échecs d'authentification (#495).
- Correction de vulnérabilités XSS (#520).
- Correction de problèmes liés aux variables d'environnement Scalingo (#76c8dd3).
- Correction de problèmes liés aux invites (#27661e7).
- Correction de problèmes liés au nom de l'application Celery (#af83580).
- Correction de problèmes liés à la suppression d'images orphelines (#532).
- Correction d'un bug de positionnement du curseur dans les combobox (#534).
- Configuration des en-têtes Orval pour supprimer les informations de version (#530).
- Mise à jour des chaînes de traduction (#03387b6, #b625507).
- Mise à jour des dépendances frontend (#eef8793).
- Ajout de tests de fuzzing et correction de cas limites dans le parser d'email (#507).
- Correction d'erreurs "DUPLICATE" lors de la vérification des enregistrements SPF (#521).
