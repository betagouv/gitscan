## Changelog : messages (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment la gestion des boîtes de réception et la composition des messages. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application, en particulier concernant l'importation d'emails et la gestion des calendriers. Une refonte technique majeure a également été entreprise, remplaçant Next.js par Vite et TanStack Router pour optimiser les performances et la maintenabilité du frontend.

### Évolutions fonctionnelles
- **Boîte de réception :** Amélioration du menu déroulant des boîtes de réception [#705].
- **Paramètres de la boîte de réception :** Regroupement des paramètres de la boîte de réception dans une boîte de dialogue dédiée.
- **Traduction :** Ajout d'une variable `user_name` intégrée et traduction du placeholder de template.
- **Composition de message :** Amélioration de l'expérience de composition de message, notamment avec la prévisualisation des pièces jointes.
- **Liens profonds vers les threads :** Ajout de la possibilité de créer des liens directs vers des threads spécifiques [#664].
- **Assignation de threads :** Possibilité d'assigner des threads à des utilisateurs [#645].
- **Calendrier :** Ajout d'un lien vers une instance CalDAV pour accepter les événements directement [#584].
- **Illustration de la page d'accueil :** Nouvelle illustration pour la page d'accueil [#702].

### Évolutions techniques
- **Refonte Frontend :** Remplacement de Next.js par Vite et TanStack Router pour une meilleure performance et une architecture plus moderne [#675].
- **Bibliothèque JMAP Email :** Extraction du parser et du compositeur d'emails dans une nouvelle bibliothèque `jmap-email` [#700].
- **Stockage des blobs :** Implémentation d'un stockage en niveaux pour les blobs et les pièces jointes.
- **Sécurité SMTP :** Renforcement de la configuration de la connexion SMTP et des proxys.
- **Optimisation des performances :** Correction d'un problème de performance lié au nombre élevé de destinataires [#672].
- **Suppression de code obsolète :** Suppression des champs de modèle dépréciés.
- **Utilisation de LaGaufreV2 :** Utilisation du composant LaGaufreV2.

### Autres changements
- **Documentation :** Ajout de scripts de publication PyPI pour `jmap-email` [#694].
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26 [#689].
- **Corrections de bugs :** Diverses corrections de bugs concernant l'importation de PST, le traitement des statuts de livraison, la détection de Mbox, le parsing d'emails, et le calendrier.
- **Sécurité :** Ajout de la bibliothèque `defusedxml` pour une meilleure sécurité lors du traitement des fichiers XML [#677].
- **Administration :** Ajout d'un champ TOTP obligatoire et d'un champ de recherche dans l'interface d'administration [#667].
