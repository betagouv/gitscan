## Changelog : messages (30 derniers jours, au 19 juin 2026)

### Résumé
Les 30 derniers jours ont été marqués par une refonte technique majeure avec le passage de Next.js à Vite et TanStack Router, améliorant ainsi les performances et la maintenabilité du frontend. De nombreuses corrections de bugs ont été apportées, notamment concernant la composition des emails, la gestion des calendriers, la sécurité et l'importation de boîtes aux lettres. Des améliorations significatives ont également été apportées à l'expérience utilisateur, comme la gestion des brouillons, les paramètres de boîte aux lettres et la prévisualisation des pièces jointes.

### Évolutions fonctionnelles
- Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- Ajout d'un lien vers une instance CalDAV pour accepter directement les événements.
- Amélioration de l'expérience d'envoi de messages.
- Prévisualisation des pièces jointes.
- Possibilité de créer un compte sans synchronisation d'identité.
- Amélioration de la navigation dans les threads et de l'expérience utilisateur du multiselect.
- Affinement du menu déroulant des boîtes aux lettres.
- Traduction des espaces réservés des modèles et ajout de la variable `user_name`.
- Regroupement des paramètres de la boîte aux lettres dans une boîte de dialogue.
- Amélioration de l'affichage des événements récurrents avec exceptions.
- Ajout d'un rapport de l'état de l'auto-vérification à Sentry.

### Évolutions techniques
- Refonte du frontend : remplacement de Next.js par Vite et TanStack Router [#675].
- Déplacement du parser et du compositeur d'emails vers la nouvelle librairie `jmap-email` [#700].
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Utilisation du composant `LaGaufreV2`.
- Mise à jour de `dompurify` vers la dernière version.
- Mise à jour de `django-lasuite` vers la version 0.0.26 [#689].
- Ajout de `defusedxml` comme dépendance.
- Suppression des champs de modèle dépréciés liés à la migration du stockage en niveaux.

### Autres changements
- Correction d'un problème de code en dur du paramètre `lang=en` qui pouvait déclencher une traduction automatique.
- Correction de l'ajout de l'en-tête `To` aux emails sortants qui en étaient dépourvus [#712].
- Correction de problèmes liés au compositeur.
- Correction de problèmes de désépinglage des threads lors de la suppression d'un brouillon.
- Correction de problèmes liés à la gestion des pièces jointes `message/delivery-status`.
- Correction de la persistance du nom de la boîte aux lettres lorsqu'un contact est manquant.
- Correction d'un problème de permission de socket Milter au démarrage.
- Renforcement de la sécurité de la connexion SMTP et de la configuration des proxies.
- Renforcement de la sécurité de l'analyse des emails entrants.
- Correction de la détection de fichiers Mbox en tant que `text/html` avec certaines versions de libmagic [#696].
- Correction d'un problème de validation TLS opportuniste contre des MX avec des certificats incompatibles [#687].
- Correction d'un bug dans l'ordre et la sélection par défaut du calendrier lors de la réponse à un événement [#699].
- Ajout de contrôles de santé lprobe et de vérification des sommes de contrôle pour lprobe + Caddy.
