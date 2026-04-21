## Changelog : docs (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité, la correction de bugs et l'ajout de fonctionnalités pratiques pour les utilisateurs. Des améliorations significatives ont été apportées à l'accessibilité du site, notamment pour les lecteurs d'écran, ainsi que des corrections pour améliorer la stabilité et l'expérience utilisateur globale. L'ajout d'un lien vers la documentation dans le menu d'aide facilite l'accès aux ressources d'aide.

### Évolutions fonctionnelles
- Ajout d'un lien vers la documentation dans le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Affichage de Crisp (chat d'assistance) depuis le menu d'aide. [#2222](https://github.com/suitenumerique/docs/issues/2222)
- Possibilité d'ouvrir les liens internes (interlinks) avec le bouton central de la souris, Ctrl ou Cmd. [#2170](https://github.com/suitenumerique/docs/issues/2170)
- Amélioration de la gestion des documents épinglés, désormais triés par date de dernière mise à jour. [#2028](https://github.com/suitenumerique/docs/issues/2028)
- Ajout d'un indicateur visuel pour le nombre minimum de caractères requis pour la recherche. [#2064](https://github.com/suitenumerique/docs/issues/2064)

### Évolutions techniques
- Refactorisation des tests E2E pour une meilleure organisation et une exécution plus rapide. [#2142](https://github.com/suitenumerique/docs/issues/2142)
- Amélioration de la gestion des erreurs 5xx avec redirection vers une page dédiée et structuration des alertes. [#2128](https://github.com/suitenumerique/docs/issues/2128)
- Optimisation de la gestion des websockets avec ajout d'un délai aléatoire pour les reconnexions. [#2162](https://github.com/suitenumerique/docs/issues/2162)
- Correction d'une condition de course dans l'importation CSV des demandes de réconciliation. [#2153](https://github.com/suitenumerique/docs/issues/2153)
- Amélioration de la gestion des accès lors de la création de documents pour un propriétaire. [#2124](https://github.com/suitenumerique/docs/issues/2124)
- Correction d'une exception non gérée dans le validateur d'URL. [#2083](https://github.com/suitenumerique/docs/issues/2083)
- Mise à jour des dépendances Axios, Next.js, Lodash, PyJWT et Requests pour corriger des failles de sécurité.
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Ajout d'un workflow CI pour les tests E2E.
- Ajout d'un modèle de PR avec une checklist IA.

### Autres changements
- Correction de fautes de frappe dans le fichier `contributing.md`.
- Mise à jour des chaînes de traduction.
- Ajout d'un favicon par défaut.
- Ajout d'un easter egg lors de la création d'emojis de documents.
- Amélioration de la structure et de la lisibilité du fichier `CHANGELOG.md`.
- Ajout d'un template de PR avec une checklist IA.
- Mise à jour de la documentation et des commentaires du code.
- Amélioration de l'accessibilité de l'interface utilisateur pour les lecteurs d'écran (ARIA, focus, etc.).
- Correction de plusieurs problèmes d'accessibilité liés à l'exportation HTML, aux menus déroulants et aux boutons.
- Suppression des paramètres UTM des URLs.
