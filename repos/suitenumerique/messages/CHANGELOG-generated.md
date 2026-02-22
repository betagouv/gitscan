## Changelog : messages (30 derniers jours)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'importation et l'exportation de boîtes aux lettres, ainsi que des optimisations de l'interface utilisateur, notamment pour l'éditeur de signature et la composition de messages. Des corrections de bugs et des améliorations de sécurité ont également été implémentées, ainsi que des améliorations de la surveillance et de la gestion des tâches en arrière-plan.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter une boîte aux lettres au format MBOX, avec prise en charge des libellés (#553).
- Prise en charge de l'importation de fichiers PST et diffusion des données pour l'importation MBOX (#544).
- Ajout d'une liste noire pour les préfixes de boîtes aux lettres personnelles (#540).
- Ajout d'un bouton d'impression dans le menu contextuel des messages (#518).
- Possibilité d'ajouter des images directement dans le corps des messages via l'éditeur BlockNote (#511, #81db181).
- Ajout de la possibilité de joindre des pièces jointes lors du renvoi d'un message (#485).
- Ajout d'une vue "Intégrations" dans les paramètres de la boîte aux lettres (#488).
- Affichage des invitations de calendrier dans les messages (#481).
- Ajout d'un dossier "Sortie" conditionnel (#550).
- Amélioration de la formulation dans la boîte de sortie (#539).
- Ajout d'une option d'autofocus dans les compositeurs de messages, modèles et signatures (#527).
- Amélioration de l'éditeur de signature avec une disposition en plusieurs colonnes (#551).
- Personnalisation des menus de l'éditeur et du panneau latéral (#548).
- Utilisation du nom d'affichage pour les libellés et dépliement automatique des parents actifs (#547).

### Évolutions techniques
- Ajout du throttling des destinataires des messages sortants (#506).
- Utilisation d'un webhook et d'une journalisation au lieu d'une pushgateway pour les auto-vérifications du MDA (#550).
- Mise à niveau des étapes du workflow GitHub Actions (#555).
- Ajout de la prise en charge de la plateforme ARM64 pour les builds d'images Docker (#554).
- Activation des événements de tâches Celery pour la surveillance des workers (#549).
- Optimisation de la sérialisation de MessageTemplate et de la gestion du corps (#545).
- Mise à niveau de django-lasuite de 0.0.19 à 0.0.24 (#546).
- Renforcement des contrôles DNS et ajout d'enregistrements configurables (#522).
- Ajout de tests de fuzzing et correction de quelques cas limites dans le parser d'emails (#507).
- Refactorisation du code des permissions pour les viewsets (#503).
- Ajout d'une commande `worker.py` et amélioration du routage des tâches sur les queues (#504).
- Utilisation du cache Redis pour le développement (#515).

### Autres changements
- Correction de bugs liés à la suppression d'attachments orphelins dans les brouillons (#532).
- Correction d'un bug de positionnement du curseur dans les champs de saisie des combobox (#534).
- Configuration des en-têtes Orval pour supprimer les informations de version (#530).
- Correction de problèmes liés aux erreurs SSL et à l'échec de l'authentification (#495).
- Ajout de protections contre les vulnérabilités XSS (#520).
- Correction d'une fuite de mémoire lors de l'importation de fichiers MBOX volumineux (#516).
- Correction de problèmes liés à la surcharge de la variable d'environnement Celery (#76c8dd3).
- Correction d'un bug lié au nom par défaut des invitations .ics (#27661e7).
- Traduction de nombreuses variantes françaises (#03387b6).
- Mise à jour des chaînes de caractères traduites (#ee32351).
- Bump de Keycloak vers la version 26.5.3 (#543).
