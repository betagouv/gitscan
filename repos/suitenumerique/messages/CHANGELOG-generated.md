## Changelog : messages (30 derniers jours, au 24 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment au niveau de la composition des emails, de la gestion des brouillons et de la navigation dans les fils de discussion. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la sécurité de l'application, ainsi que des optimisations techniques importantes comme le passage à Vite et TanStack Router pour l'interface utilisateur.

### Évolutions fonctionnelles
- Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- Création de boîtes aux lettres sans mot de passe lorsque la synchronisation d'identité est désactivée. [#707](https://github.com/suitenumerique/messages/issues/707)
- Regroupement des paramètres de la boîte aux lettres dans une boîte de dialogue.
- Traduction des espaces réservés des modèles et ajout de la variable intégrée `user_name`.
- Amélioration de l'expérience d'envoi d'emails.
- Ajout de l'en-tête `To` aux emails sortants qui en étaient dépourvus. [#712](https://github.com/suitenumerique/messages/issues/712)
- Correction de l'affichage des événements récurrents avec des exceptions. [#686](https://github.com/suitenumerique/messages/issues/686)
- Correction de l'ordre et de la sélection par défaut du calendrier lors de la réponse aux invitations. [#699](https://github.com/suitenumerique/messages/issues/699)
- Correction d'un problème d'affichage des sauts de ligne dans le composeur sur Chrome Android. [#725](https://github.com/suitenumerique/messages/issues/725)

### Évolutions techniques
- Migration de Next.js vers Vite et TanStack Router pour l'interface utilisateur. [#675](https://github.com/suitenumerique/messages/issues/675)
- Déplacement du parser et du compositeur d'emails vers la nouvelle librairie `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- Mise à jour de `django-lasuite` vers la version 0.0.27.
- Mise à jour de Keycloak vers la version 26.6.3. [#718](https://github.com/suitenumerique/messages/issues/718)
- Mise à jour de `dompurify` vers la dernière version.
- Amélioration de la navigation dans les fils de discussion et de l'UX de la sélection multiple. [#708](https://github.com/suitenumerique/messages/issues/708)
- Amélioration du menu déroulant des boîtes aux lettres. [#705](https://github.com/suitenumerique/messages/issues/705)
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Utilisation du composant `LaGaufreV2`.
- Internationalisation des chaînes de caractères manquantes.

### Autres changements
- Ajout de mesures de sécurité supplémentaires (defense-in-depth). [#706](https://github.com/suitenumerique/messages/issues/706)
- Renforcement de la connexion SMTP et de la configuration des proxys.
- Correction d'un problème de permission de socket milter au démarrage. [#693](https://github.com/suitenumerique/messages/issues/693)
- Correction d'un problème de détection de mbox en tant que text/html avec certaines versions de libmagic. [#696](https://github.com/suitenumerique/messages/issues/696)
- Correction d'un problème lié aux pièces jointes de type `message/delivery-status`.
- Correction d'un problème de persistance du nom de la boîte aux lettres lorsque le contact est manquant.
- Suppression d'un attribut inutile `perspective`. [#709](https://github.com/suitenumerique/messages/issues/709)
- Ajout de rapports d'état de l'auto-vérification à Sentry. [#694](https://github.com/suitenumerique/messages/issues/694)
- Installation de `jmap-email` depuis PyPI. [#711](https://github.com/suitenumerique/messages/issues/711)
- Correction d'un bug empêchant le déchargement immédiat de la vue du fil de discussion lors de sa désélection.
- Correction d'un bug empêchant le rechargement des messages du fil de discussion lors de la suppression d'un brouillon.
