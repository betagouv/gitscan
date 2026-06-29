## Changelog : messages (30 derniers jours, au 24 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment dans la composition des emails, la gestion des brouillons et la navigation entre les fils de discussion. Des corrections de bugs et des améliorations de sécurité ont également été implémentées, ainsi qu'une refonte technique majeure avec le passage à Vite et TanStack Router pour le frontend.

### Évolutions fonctionnelles
- Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- Création de boîtes de réception sans mot de passe possible lorsque la synchronisation d'identité est désactivée [#707].
- Regroupement des paramètres de la boîte de réception dans une boîte de dialogue.
- Traduction des espaces réservés des modèles et ajout de la variable intégrée `user_name`.
- Amélioration de la navigation entre les fils de discussion et de la sélection multiple [#708].
- Affinement du menu déroulant des boîtes de réception [#705].
- Nouvelle illustration pour la page d'accueil [#702].
- Ajout de l'en-tête `To` aux emails sortants qui en étaient dépourvus [#712].
- Correction d'un problème d'affichage des événements récurrents avec des exceptions.
- Correction d'un problème de saut de ligne dans le compositeur sur Chrome Android [#725].

### Évolutions techniques
- Refonte du frontend : remplacement de Next.js par Vite et TanStack Router [#675].
- Déplacement de l'analyseur et du compositeur d'emails vers la nouvelle bibliothèque `jmap-email` [#700].
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Utilisation du composant `LaGaufreV2`.
- Amélioration de la gestion des pièces jointes dans le compositeur.
- Mise à jour de la bibliothèque `dompurify`.
- Mise à jour de `django-lasuite` à la version 0.0.27.
- Mise à jour de Keycloak à la version 26.6.3 [#718].

### Autres changements
- Ajout de rapports d'état de l'auto-vérification à Sentry [#694].
- Renforcement de la sécurité de la connexion SMTP et de la configuration des proxys.
- Renforcement de l'analyse des emails entrants [#695].
- Correction d'un problème de concurrence de permissions de socket milter au démarrage [#693].
- Correction d'un problème de détection de mbox comme `text/html` avec certaines versions de libmagic [#696].
- Correction d'un problème de chargement des certificats TLS opportunistes [#687].
- Correction d'un problème de persistance du nom de la boîte de réception lorsque le contact est manquant.
- Correction d'un problème d'ordre et de sélection par défaut du calendrier lors de la confirmation de présence [#699].
- Correction d'un attribut inutile dans le frontend.
- Internationalisation des chaînes de caractères manquantes.
- Amélioration de l'accessibilité de la navigation entre les fils de discussion.
- Amélioration des paramètres de la boîte de réception.
- Mise à jour de la liste des préfixes de dossiers d'emails PST.
