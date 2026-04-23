## Changelog : docs (30 derniers jours, au 21 avril 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'interlinking, de la gestion des membres sur les petits écrans et de la correction de bugs affectant la stabilité et l'ergonomie de l'application. Des améliorations significatives ont également été apportées à l'accessibilité, rendant l'outil plus inclusif. Enfin, des optimisations ont été réalisées au niveau du CI/CD et de la sécurité.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Intégration de Crisp (outil de chat) via le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Amélioration de l'UX/UI de l'interlinking.
- Possibilité d'ouvrir les liens internes (interlinks) avec le bouton central de la souris ou la touche Ctrl/Cmd.
- Amélioration de la gestion des membres sur les petits écrans.
- Ajout d'un easter egg lors de la création d'emojis.
- Possibilité de trier les documents épinglés par date de dernière mise à jour. [#2028](https://github.com/suitenumerique/docs/issues/2028)
- Ajout d'un indicateur visuel pour le nombre minimum de caractères pour la recherche.

### Évolutions techniques
- Factorisation des tests E2E dans un workflow séparé pour améliorer la performance du CI.
- Ajout d'un flag pour indiquer si les tests E2E ont échoué lors de la dernière exécution.
- Mise à jour de la dépendance Axios vers la version 1.15.0 (correction de sécurité).
- Mise à jour de la dépendance Next.js vers la version 16.2.3 (correction de sécurité).
- Mise à jour de la dépendance PyJWT vers la version 2.12.0.
- Mise à jour de la dépendance lodash vers la version 4.18.1 (correction de sécurité).
- Mise à jour de la dépendance requests vers la version 2.33.0 (correction de sécurité).
- Amélioration de la gestion de la mémoire pour le provider Yjs.
- Refonte de la structure des alertes d'erreur 5xx pour une meilleure accessibilité.
- Ajout d'un favicon par défaut.
- Correction d'un problème de rechargement superficiel de l'application.
- Suppression d'une ligne horizontale inutile lorsque aucun élément n'est présent.
- Correction de la position de l'interlinking lors de la perte de focus.
- Correction d'un problème de clipping du modal d'interlinking.
- Correction d'un bug lié à la gestion des effets de bord entre les commentaires et le versionning.
- Correction d'un bug lié à la création de colonnes avec le curseur.
- Amélioration de la compatibilité des tests E2E avec différentes instances.
- Optimisation de l'exécution des tests E2E pour ne rejouer que les tests ayant échoué.
- Ajout de niveaux de permissions au workflow CI.
- Correction d'un problème de redirection après une erreur 401.
- Ajout d'un mécanisme de verrouillage pour éviter les conditions de concurrence dans l'action `create_for_owner`.
- Correction d'une exception inatteignable dans le validateur d'URL.
- Correction d'une condition de concurrence lors de l'importation de CSV pour la réconciliation.

### Autres changements
- Correction de fautes de frappe dans le fichier `contributing.md`.
- Ajout d'une checklist IA au template de pull request.
- Refonte et ajout d'une politique IA au fichier `contributing.md`.
- Mise à jour des chaînes de traduction.
- Ajout d'un flag de fonctionnalité pour l'importation de documents.
- Exposition de la variable `CONVERSION_UPLOAD_ENABLED` dans l'endpoint de configuration.
- Ajout de logs pour tracer les conversions effectuées lors de la création de documents.
- Correction de problèmes d'accessibilité liés aux résultats de recherche de documents.
- Correction de problèmes d'accessibilité liés aux erreurs 5xx.
- Amélioration de l'accessibilité des menus déroulants et des boutons.
- Amélioration de l'accessibilité des listes et de la navigation au clavier.
- Ajout d'instructions pour les lecteurs d'écran.
- Correction de problèmes d'accessibilité liés à l'exportation au format HTML.
- Ajout d'attributs ARIA pour améliorer l'accessibilité.
- Suppression des paramètres UTM des URLs.
- Mise à jour des dépendances BlockNote.
- Correction d'erreurs et d'avertissements ESLint.
- Ajout de nginx-frontend.
- Ajout de la page de réconciliation sur nginx.
- Correction de bugs et amélioration de la qualité du code.
