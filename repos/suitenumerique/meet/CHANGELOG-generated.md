## Changelog : meet (30 derniers jours, au 30 juin 2026)

### Résumé
Les dernières mises à jour de Meet se concentrent sur l'amélioration de l'expérience utilisateur, notamment en ajoutant des fonctionnalités comme le partage d'écran en mode image dans l'image, des améliorations de l'accessibilité, et des correctifs pour la gestion des fichiers et des utilisateurs. Des efforts importants ont également été déployés pour renforcer la sécurité et la stabilité de la plateforme, ainsi que pour optimiser les performances et la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout du partage d'écran en mode image dans l'image (PiP) [#1458](https://github.com/suitenumerique/meet/issues/1458).
- Amélioration de la gestion des fichiers avec l'ajout d'une interface d'administration spécifique.
- Possibilité de masquer le bouton de connexion via un paramètre d'URL.
- Possibilité de désactiver la connexion silencieuse via un paramètre d'URL.
- Ajout d'un sondage de satisfaction optionnel en bas des résumés de réunion.
- Amélioration de la réduction du bruit avec un pipeline audio BBBA.
- Mise en place d'un comportement par défaut de mise en sourdine des participants lors de l'entrée dans une grande réunion.
- Suppression du son de notification lors de l'entrée dans une grande réunion.
- Ajout d'une commande pour fusionner les utilisateurs en double.
- Ajout d'un job Kubernetes pour automatiser la fusion des utilisateurs en double.
- Amélioration de l'add-on Outlook avec la prise en charge de l'i18n, un lien de feedback et une insertion plus intelligente du lien de réunion.

### Évolutions techniques
- Refactorisation de la gestion des variables d'environnement.
- Mise à jour de plusieurs dépendances, notamment `react-i18next`, `aiohttp`, `idna`, `urllib3`, et les dépendances frontend.
- Amélioration de la robustesse du processus de suppression des fichiers.
- Changement de la méthode de gestion de l'état des fichiers pour éviter les blocages de longue durée.
- Mise à jour du modèle de transcription par défaut pour le résumé.
- Ajout d'un fallback pour l'enregistrement des réunions en cas de problème avec les webhooks S3/MinIO.
- Amélioration de la gestion des erreurs lors de la fermeture du collecteur de métadonnées.
- Utilisation de `ReturnType<typeof setTimeout>` pour améliorer la typage.
- Amélioration de la configuration de la journalisation.
- Optimisation de la gestion des dépendances de l'add-on Outlook.
- Lazy-load de `@libreaudio/la-call` pour améliorer les performances.
- Mise à jour des images Docker uniquement sur les tags de release.
- Correction de régressions CSP (Content Security Policy) affectant les styles en ligne et ProConnect.
- Mise à jour des versions des bibliothèques `libcrypto3` et `libssl3`.

### Autres changements
- Ajout du badge DPG au README.
- Clarification des directives de contribution dans le README.
- Ajout de Clever Cloud à la liste des fournisseurs SaaS La Suite Meet.
- Ajout de l'instance email.eu à la liste des instances connues.
- Mise à jour de la documentation pour refléter la refonte de l'icône via un volume monté.
- Mise à jour de la documentation pour préciser la généralisation française par le chef de produit.
- Mise à jour de la version de la release à 1.21.0 et 1.20.0.
- Amélioration de l'accessibilité des effets visuels et de la structure du panneau de contrôle de pagination.
- Correction de bugs liés à l'affichage des options et à l'état du collecteur d'agents.
- Amélioration de l'accessibilité des arrière-plans personnalisés.
- Correction de l'étiquette ARIA pour les effets de flou.
- Mise à jour du chart Helm.
- Correction d'un bug lié à l'affichage des agents de métadonnées.
- Bump de la version du plugin addon à 0.0.2.
- Internationalisation de l'addon.
- Ajout d'un formulaire de feedback dans le footer de l'addon.
- Correction d'un bug empêchant la fermeture automatique des dialogues.
- Correction d'un bug lié à l'insertion du lien de réunion.
- Correction d'un bug lié à l'affichage du bouton d'ajout de lien.
- Épingle des dépendances de l'addon à leurs versions actuelles.
