## Changelog : messages (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de la performance et de l'expérience utilisateur de Messages. Les améliorations incluent une meilleure gestion des pièces jointes, une navigation plus accessible, des corrections de bugs importants et une refonte technique majeure pour moderniser l'interface utilisateur. Des améliorations de la sécurité ont également été apportées, notamment au niveau de la configuration SMTP et de la gestion des certificats.

### Évolutions fonctionnelles
- **Threads :** Suppression définitive des brouillons et amélioration de l'édition des brouillons. [#707](https://github.com/suitenumerique/messages/issues/707)
- **Calendrier :** Possibilité de lier une instance CalDAV pour accepter directement les événements. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Pièces jointes :** Prévisualisation des pièces jointes. [#676](https://github.com/suitenumerique/messages/issues/676)
- **Boîtes de réception :** Amélioration de la navigation et de l'accessibilité des boîtes de réception, notamment avec l'utilisation de menus déroulants améliorés. [#705](https://github.com/suitenumerique/messages/issues/705) et [#708](https://github.com/suitenumerique/messages/issues/708)
- **Composer :** Amélioration de l'expérience de composition des messages.
- **Assignation de threads :** Possibilité d'assigner des threads à des utilisateurs. [#645](https://github.com/suitenumerique/messages/issues/645)
- **Paramètres de la boîte de réception :** Regroupement des paramètres de la boîte de réception dans une boîte de dialogue. [#702](https://github.com/suitenumerique/messages/issues/702)
- **Création de boîte aux lettres :** Possibilité de créer une boîte aux lettres sans mot de passe lorsque la synchronisation d'identité est désactivée. [#707](https://github.com/suitenumerique/messages/issues/707)

### Évolutions techniques
- **Frontend :** Migration de Next.js vers Vite et TanStack Router pour moderniser l'architecture frontend et améliorer les performances. [#675](https://github.com/suitenumerique/messages/issues/675)
- **Bibliothèque email :** Refactorisation du parser et du compositeur d'emails vers une nouvelle bibliothèque `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- **Stockage des blobs :** Implémentation d'un stockage en plusieurs niveaux pour les blobs et les pièces jointes.
- **Sécurité SMTP :** Renforcement de la configuration de la connexion SMTP et des proxys.
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26. [#689](https://github.com/suitenumerique/messages/issues/689)
- **Architecture :** Suppression des champs de modèle dépréciés.
- **Performance :** Optimisation des requêtes N+1 dans l'interface d'administration et des recherches lentes.

### Autres changements
- Correction d'un bug empêchant l'ajout de l'en-tête `To` aux emails sortants. [#712](https://github.com/suitenumerique/messages/issues/712)
- Correction de bugs liés à l'importation de fichiers MBOX et PST.
- Amélioration de la gestion des statuts de vérification de la messagerie (delivery status).
- Ajout de scripts de publication PyPI pour la bibliothèque `jmap-email`.
- Amélioration de la gestion des erreurs et des logs.
- Internationalisation de chaînes de caractères manquantes.
- Mise à jour de la documentation.
- Correction de bugs divers liés à l'interface utilisateur et à la gestion des threads.
