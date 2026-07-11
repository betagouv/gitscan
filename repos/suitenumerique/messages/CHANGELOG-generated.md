## Changelog : messages (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la sécurité, de la robustesse et de l'expérience utilisateur. Des corrections importantes ont été apportées au traitement des emails entrants, à la gestion des pièces jointes et à la sécurité globale. L'interface utilisateur a également été améliorée avec des corrections de bugs et des ajustements pour une meilleure accessibilité.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage des retours à la ligne dans le compositeur sur les appareils Android. [#725](https://github.com/suitenumerique/messages/issues/725)
- Amélioration de la navigation dans les threads et de l'expérience utilisateur pour la sélection multiple. [#708](https://github.com/suitenumerique/messages/issues/708)
- Affichage du nombre de messages non lus dans le menu déroulant des boîtes de réception.
- Suppression définitive des brouillons et amélioration de l'édition des brouillons.
- Possibilité de créer des boîtes de réception sans synchronisation d'identité. [#707](https://github.com/suitenumerique/messages/issues/707)
- Amélioration des paramètres de la boîte de réception.
- Détection des liens hypertextes dans le corps HTML des emails et avertissement avant redirection. [#744](https://github.com/suitenumerique/messages/issues/744)
- Réinitialisation de la recherche lors du changement de boîte de réception. [#743](https://github.com/suitenumerique/messages/issues/743)
- Correction d'un problème de wrapping prématuré des lignes dans le compositeur. [#740](https://github.com/suitenumerique/messages/issues/740)

### Évolutions techniques
- Refonte complète du MTA-in en Python pur pour supprimer la dépendance à Postfix. [#692](https://github.com/suitenumerique/messages/issues/692)
- Ajout d'une liste blanche d'hôtes pour contourner les problèmes SSRF dans les réseaux internes.
- Utilisation de la méthode intégrée pour générer l'ID des messages. [#730](https://github.com/suitenumerique/messages/issues/730)
- Ajout d'un en-tête X-Mailer aux emails sortants.
- Configuration du frontend à partir du backend. [#734](https://github.com/suitenumerique/messages/issues/734)
- Mise à jour de la bibliothèque `django-lasuite` vers la version 0.0.27.
- Mise à jour de la bibliothèque `keycloak` vers les versions 26.6.3 et 26.6.4. [#718](https://github.com/suitenumerique/messages/issues/718), [#729](https://github.com/suitenumerique/messages/issues/729), [#732](https://github.com/suitenumerique/messages/issues/732)
- Suppression du composant `react-email`.
- Amélioration du traitement des messages entrants via l'administration.
- Sauvegarde de l'adresse IP d'origine lors des redémarrages STARTTLS.
- Ajout de webhooks, de balises de message et de corrections anti-spam.
- Ajout de contrôles de sécurité supplémentaires. [#706](https://github.com/suitenumerique/messages/issues/706)
- Correction d'un problème de langue codée en dur pouvant déclencher une traduction automatique. [#695](https://github.com/suitenumerique/messages/issues/695)

### Autres changements
- Linting des sous-projets.
- Installation de la bibliothèque `jmap-email` à partir de PyPI. [#711](https://github.com/suitenumerique/messages/issues/711)
- Correction de l'indentation du bloc relay dans `main.cf.j2`. [#733](https://github.com/suitenumerique/messages/issues/733)
- Mise à jour de `dompurify` vers la dernière version.
