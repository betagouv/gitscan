## Changelog : messages (30 derniers jours, au 7 juillet 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de la configuration, la correction de bugs et l'optimisation de la gestion des emails entrants et sortants. Des améliorations significatives ont été apportées à l'interface utilisateur, notamment au niveau de la navigation dans les threads et de la gestion des brouillons. Une refonte majeure de la gestion des emails entrants a été effectuée en remplaçant Postfix par une solution purement Python.

### Évolutions fonctionnelles
- L'interface utilisateur a été améliorée pour la navigation dans les threads et la sélection multiple, notamment en termes d'accessibilité. [#708](https://github.com/suitenumerique/messages/issues/708)
- Le menu déroulant des boîtes de réception a été affiné pour une meilleure expérience utilisateur. [#705](https://github.com/suitenumerique/messages/issues/705)
- Un compteur d'emails non lus est maintenant affiché dans le menu déroulant des boîtes de réception.
- Les paramètres de la boîte de réception sont désormais regroupés dans une boîte de dialogue dédiée.
- Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- Amélioration de la gestion des noms de boîtes de réception lorsque le contact est manquant. [#710](https://github.com/suitenumerique/messages/issues/710)
- Possibilité de créer des boîtes de réception sans mot de passe lorsque la synchronisation d'identité est désactivée. [#707](https://github.com/suitenumerique/messages/issues/707)
- Correction d'un problème d'espacement des lignes dans le compositeur sur les appareils Android Chrome. [#725](https://github.com/suitenumerique/messages/issues/725)
- Correction d'un problème de saut de ligne dans le compositeur. [#740](https://github.com/suitenumerique/messages/issues/740)
- Correction d'un problème de sélection non interactive des éléments de thread. [#714](https://github.com/suitenumerique/messages/issues/714)
- Suppression des threads épinglés lors de la suppression d'un brouillon.
- Ajout d'une nouvelle illustration pour la page d'accueil. [#702](https://github.com/suitenumerique/messages/issues/702)

### Évolutions techniques
- La configuration du frontend est désormais récupérée depuis le backend. [#734](https://github.com/suitenumerique/messages/issues/734)
- Suppression de la dépendance à Postfix pour la gestion des emails entrants, remplacée par une solution purement Python. [#692](https://github.com/suitenumerique/messages/issues/692)
- Refonte du frontend avec Vite et TanStack Router, abandonnant Next.js. [#675](https://github.com/suitenumerique/messages/issues/675)
- Déplacement de l'analyseur et du compositeur d'emails vers une nouvelle bibliothèque `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- Ajout d'une liste d'autorisation d'hôtes pour contourner les problèmes SSRF dans les réseaux internes.
- Amélioration du re-traitement des messages entrants depuis l'administration.
- Sauvegarde de l'adresse IP d'origine lors des redémarrages STARTTLS.
- Ajout de webhooks, de balises de message et de corrections anti-spam.
- Ajout de l'en-tête X-Mailer aux emails sortants.
- Mise à jour de la bibliothèque `django-lasuite` vers la version 0.0.27.
- Mise à jour de Keycloak vers les versions 26.6.3 et 26.6.4. [#718](https://github.com/suitenumerique/messages/issues/718), [#729](https://github.com/suitenumerique/messages/issues/729), [#732](https://github.com/suitenumerique/messages/issues/732)
- Suppression du composant `react-email`.
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Correction d'un problème de langue codée en dur pouvant déclencher une traduction automatique. [#695](https://github.com/suitenumerique/messages/issues/695)

### Autres changements
- Correction de linting sur les sous-projets.
- Suppression d'un attribut inutile dans la perspective. [#709](https://github.com/suitenumerique/messages/issues/709)
- Mise à jour de dompurify vers la dernière version.
- Ajout de mesures de sécurité et de renforcement. [#706](https://github.com/suitenumerique/messages/issues/706)
- Correction de l'indentation du bloc relay dans main.cf.j2. [#733](https://github.com/suitenumerique/messages/issues/733)
- Réinitialisation de la recherche lors du changement de boîte de réception. [#743](https://github.com/suitenumerique/messages/issues/743)
