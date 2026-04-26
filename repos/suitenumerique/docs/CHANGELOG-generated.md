## Changelog : docs (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'interlinking, de la gestion des membres et de l'accessibilité. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application. Des améliorations techniques ont été réalisées sur le CI/CD et la gestion des tests.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Amélioration de l'UX/UI de l'interlinking (liens internes).
- Possibilité d'ouvrir les liens internes avec le bouton du milieu de la souris ou avec Ctrl/Cmd + clic. [#2170](https://github.com/suitenumerique/docs/issues/2170)
- Amélioration de la gestion des membres sur les petits écrans. [#2226](https://github.com/suitenumerique/docs/issues/2226)
- Ajout d'un indicateur visuel pour les documents épinglés, triés par date de dernière modification. [#2028](https://github.com/suitenumerique/docs/issues/2028)
- Ajout d'un easter egg lors de la création d'emojis de documents. [#2155](https://github.com/suitenumerique/docs/issues/2155)
- Ajout d'un indicateur visuel pour les documents épinglés, triés par date de dernière modification.

### Évolutions techniques
- Refactorisation des tests E2E pour une meilleure compatibilité et une exécution plus rapide (exécution uniquement des tests ayant échoué lors d'une nouvelle tentative).
- Factorisation des tests E2E dans un workflow CI distinct.
- Amélioration de la gestion des erreurs 5xx avec une redirection vers une page dédiée et une structure d'alerte améliorée. [#2128](https://github.com/suitenumerique/docs/issues/2128)
- Mise à jour des dépendances : `axios`, `next`, `lodash`, `PyJWT`, `blocknote`.
- Ajout de permissions au workflow CI.
- Suppression des paramètres UTM.
- Amélioration de la gestion des websockets avec ajout d'un jitter pour les reconnexions.
- Correction d'une condition de course dans l'importation CSV des demandes de rapprochement.
- Correction d'une exception non gérée dans le validateur d'URL.

### Autres changements
- Correction de fautes de frappe dans le fichier `contributing.md`.
- Ajout d'une checklist IA au template de PR.
- Amélioration de la documentation et de la politique de contribution.
- Améliorations de l'accessibilité (ARIA) pour divers composants de l'interface utilisateur : résultats de recherche, menus déroulants, boutons, listes, etc.
- Ajout d'un favicon par défaut.
- Mise à jour des chaînes de traduction.
- Amélioration de la structure du code et correction de warnings ESLint.
- Ajout de nginx-frontend.
- Ajout de la page de reconciliation sur nginx.
