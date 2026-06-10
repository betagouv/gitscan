## Changelog : messages (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur une refonte technique majeure du frontend, passant de Next.js à Vite et TanStack Router pour améliorer les performances et la maintenabilité. Des améliorations significatives ont également été apportées à l'importation d'emails (PST, MBOX) et à la gestion des calendriers, ainsi que des corrections de bugs et des optimisations de sécurité.

### Évolutions fonctionnelles
- **Calendrier :** Ajout de la possibilité de lier une instance CalDAV pour accepter directement les événements. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Composer :** Amélioration de l'expérience d'envoi de messages.
- **Pièces jointes :** Prévisualisation des pièces jointes. [#676](https://github.com/suitenumerique/messages/issues/676)
- **Liens profonds :** Ajout de liens profonds vers les threads. [#664](https://github.com/suitenumerique/messages/issues/664)
- **Assignation de threads :** Possibilité d'assigner des threads. [#645](https://github.com/suitenumerique/messages/issues/645)

### Évolutions techniques
- **Frontend :** Migration de Next.js vers Vite et TanStack Router pour de meilleures performances et une architecture plus moderne. [#675](https://github.com/suitenumerique/messages/issues/675)
- **Bibliothèque d'emails :** Extraction du parser et du compositeur d'emails dans une nouvelle bibliothèque `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- **Stockage des blobs :** Implémentation d'un stockage en plusieurs niveaux et refactorisation des blobs/pièces jointes.
- **SMTP :** Renforcement de la configuration de la connexion SMTP et des proxys.
- **Architecture :** Suppression des champs de modèle dépréciés. [#678](https://github.com/suitenumerique/messages/issues/678)
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26. [#689](https://github.com/suitenumerique/messages/issues/689)

### Autres changements
- Ajout de scripts de publication PyPI.
- Nouvelle illustration pour la page d'accueil. [#702](https://github.com/suitenumerique/messages/issues/702)
- Correction de l'ordre et de la sélection par défaut du calendrier lors de la confirmation de présence. [#699](https://github.com/suitenumerique/messages/issues/699)
- Correction de bugs liés à l'importation MBOX et PST. [#687](https://github.com/suitenumerique/messages/issues/687), [#696](https://github.com/suitenumerique/messages/issues/696)
- Correction de bugs liés au parsing des emails entrants. [#695](https://github.com/suitenumerique/messages/issues/695)
- Ajout de rapports d'état de l'auto-vérification à Sentry. [#694](https://github.com/suitenumerique/messages/issues/694)
- Correction d'une condition de concurrence dans le démarrage du filtre Milter. [#693](https://github.com/suitenumerique/messages/issues/693)
- Correction de l'utilisation de l'email OIDC au lieu de l'email de la boîte aux lettres pour CalDAV. [#679](https://github.com/suitenumerique/messages/issues/679)
- Correction de problèmes de performance liés au nombre élevé de destinataires. [#672](https://github.com/suitenumerique/messages/issues/672)
- Optimisation des requêtes N+1 dans l'administration.
- Ajout d'un champ TOTP obligatoire et d'un champ de recherche dans l'administration.
- Ajout de la bibliothèque `defusedxml` comme dépendance. [#677](https://github.com/suitenumerique/messages/issues/677)
