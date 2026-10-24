## Changelog : relecteur (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci, relecteur a considérablement étendu ses capacités en devenant capable d'effectuer des revues de code directement sur les Pull Requests, y compris dans les dépôts privés. L'outil d'évaluation a également été enrichi pour être plus précis, plus résilient aux limites des API d'IA, et capable de générer automatiquement des cas de test à partir de l'historique du projet.

### Évolutions fonctionnelles
- **Revue de Pull Requests (PR) :** Intégration de la revue automatique directement dans le flux de travail GitHub, avec affichage de résumés détaillés pour chaque revue au sein des checks de la PR.
- **Support des dépôts privés :** Capacité désormais étendue pour analyser les projets privés via une gestion sécurisée des jetons d'accès.
- **Configuration flexible :** Possibilité de sélectionner précisément les fichiers à réviser via le fichier de configuration `.relecteur/config.toml`.
- **Génération automatique de cas de test :** Nouvelle compétence permettant de créer des cas d'évaluation à partir de l'historique du dépôt ou des commentaires de revue existants.
- **Rapports enrichis :** Les rapports d'évaluation incluent désormais des métriques de consommation (temps moyen et nombre de tokens par revue).

### Évolutions techniques
- **Résilience accrue :** Amélioration de la gestion des erreurs réseau et des limites de débit (rate limits) des modèles d'IA, avec des mécanismes de reprise automatique des revues interrompues par un push ou un timeout.
- **Moteur d'évaluation optimisé :** Refonte du système de détection des défauts utilisant des probabilités et un nouveau composant `DefectFinder`.
- **Auto-évaluation :** Mise en place d'un pipeline CI/CD où relecteur utilise son propre moteur pour réviser ses propres Pull Requests.
- **Optimisation du traitement :** Amélioration de la performance en traitant les fichiers par groupes lors des revues à haut effort.

### Autres changements
- **Documentation :** Refonte majeure de la documentation, désormais disponible par défaut en français avec un guide de démarrage rapide structuré par audience.
- **Comparatifs :** Ajout de comparaisons documentées avec des outils tiers (Claude Code Review, CodeRabbit et Greptile) pour expliciter la valeur ajoutée de relecteur.
- **Clarification :** Précisions sur le fonctionnement du "juge" (seuil de probabilité) et sur l'utilisation des instructions de revue du dépôt.
