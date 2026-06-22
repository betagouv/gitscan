## Changelog : messages (30 derniers jours, au 19 juin 2026)

### Résumé
Les dernières mises à jour de Messages apportent des améliorations significatives à la gestion des brouillons, à la sécurité, à l'expérience utilisateur et à l'infrastructure sous-jacente. Une migration technique majeure a eu lieu avec le remplacement de Next.js par Vite et TanStack Router, offrant de meilleures performances et une architecture plus moderne. Des corrections de bugs et des améliorations de la sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- Création de boîtes aux lettres sans mot de passe possible lorsque la synchronisation d'identité est désactivée. [#707](https://github.com/suitenumerique/messages/issues/707)
- Regroupement des paramètres de la boîte aux lettres dans une boîte de dialogue.
- Traduction des espaces réservés des modèles et ajout de la variable intégrée `user_name`.
- Ajout d'un lien vers une instance CalDAV pour accepter directement les événements. [#584](https://github.com/suitenumerique/messages/issues/584)
- Prévisualisation des pièces jointes.
- Amélioration de l'expérience d'envoi de messages.
- Navigation améliorée dans les threads et expérience utilisateur multisélection. [#708](https://github.com/suitenumerique/messages/issues/708)
- Menu déroulant des boîtes aux lettres amélioré. [#705](https://github.com/suitenumerique/messages/issues/705)
- Nouvelle illustration pour la page d'accueil. [#702](https://github.com/suitenumerique/messages/issues/702)

### Évolutions techniques
- Remplacement de Next.js par Vite et TanStack Router pour une meilleure performance et une architecture plus moderne. [#675](https://github.com/suitenumerique/messages/issues/675)
- Migration du parser et du compositeur d'emails vers la nouvelle librairie `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Mise à jour de `django-lasuite` vers la version 0.0.26. [#689](https://github.com/suitenumerique/messages/issues/689)
- Mise à jour de `dompurify` vers la dernière version.
- Suppression des champs de modèle dépréciés liés à la migration du stockage en niveaux. [#678](https://github.com/suitenumerique/messages/issues/678)
- Ajout de `defusedxml` comme dépendance. [#677](https://github.com/suitenumerique/messages/issues/677)

### Autres changements
- Correction d'un problème de langue codée en dur qui pouvait déclencher une traduction automatique.
- Correction de l'ajout de l'en-tête `To` aux e-mails sortants qui en manquaient. [#712](https://github.com/suitenumerique/messages/issues/712)
- Amélioration de la gestion des pièces jointes `message/delivery-status`.
- Persistance du nom de la boîte aux lettres lorsque le contact est manquant.
- Correction de l'ordre et de la sélection par défaut du calendrier lors de la réponse aux événements. [#699](https://github.com/suitenumerique/messages/issues/699)
- Correction de l'affichage des événements récurrents avec des exceptions. [#686](https://github.com/suitenumerique/messages/issues/686)
- Correction de TLS opportuniste contre les serveurs MX avec des certificats incompatibles. [#687](https://github.com/suitenumerique/messages/issues/687)
- Correction de la détection de mbox en tant que text/html avec certaines versions de libmagic. [#696](https://github.com/suitenumerique/messages/issues/696)
- Correction d'une course de permission de socket milter au démarrage. [#693](https://github.com/suitenumerique/messages/issues/693)
- Ajout de mesures de sécurité pour renforcer la connexion SMTP et la configuration des proxys.
- Renforcement de l'analyse des e-mails entrants.
- Ajout du statut de selfcheck au Sentry. [#694](https://github.com/suitenumerique/messages/issues/694)
- Correction de problèmes liés au compositeur.
- Suppression des éléments de thread lors de la suppression d'un brouillon.
- Utilisation du composant `LaGaufreV2`.
- Enveloppement de la colonne de date de réponse automatique.
- Amélioration de l'expérience d'édition des brouillons.
