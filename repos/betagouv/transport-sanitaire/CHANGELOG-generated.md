## Changelog : transport-sanitaire (30 derniers jours, au 04/11/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'architecture du projet (passage à la version 10) visant à séparer le moteur de simulation des règles métier. Cette évolution permet une mise à jour plus fluide des règles de transport sanitaire. Pour l'utilisateur, cela se traduit par une interface plus intuitive, une meilleure gestion des documents PDF (Cerfa et fiches patients) et l'intégration des dernières règles de remboursement.

### Évolutions fonctionnelles
- **Gestion documentaire** : Amélioration de la génération et du téléchargement des documents (Cerfa et fiches patients) en PDF, incluant une fonction d'aplatissement pour garantir la compatibilité des fichiers [#86](https://github.com/betagouv/transport-sanitaire/issues/86).
- **Interface utilisateur (UI/UX)** : 
    - Modernisation des éléments de saisie (utilisation de cartes pour les cases à cocher).
    - Amélioration de la lisibilité avec une gestion dynamique de la taille du texte et l'affichage des données déjà connues pour guider l'utilisateur.
    - Ajout d'une invitation à donner un avis à la fin de la simulation [#195](https://github.com/betagouv/transport-sanitaire/issues/195).
- **Règles métier** : Intégration des nouveaux modèles de règles (v10.1.x) et prise en compte de scénarios spécifiques (ALD, mineurs, retours pénitentiaires, etc.).
- **Suivi** : Envoi des résultats de parcours ALD vers Matomo pour analyse [#269](https://github.com/betagouv/transport-sanitaire/issues/269).

### Évolutions techniques
- **Architecture** : Refonte profonde pour découpler le "socle" (moteur de simulation) du "modèle" (règles métier), améliorant la maintenabilité et la modularité du code.
- **Tests** : Augmentation significative de la couverture de tests, incluant la validation automatique des parcours de recette (N2, N4) et la conformité des documents générés.
- **Outils CLI** : Évolution de l'interface en ligne de commande pour permettre le suivi des chantiers et des tâches directement via les issues et projets GitHub [#39](https://github.com/betagouv/transport-sanitaire/issues/39).
- **Optimisation du build** : Compilation du graphe de décision directement lors de la phase de build [#257](https://github.com/betagouv/transport-sanitaire/issues/257).

### Autres changements
- **Documentation** : Mise à jour du glossaire et de la documentation technique pour refléter la nouvelle architecture et la nouvelle terminologie.
- **Nettoyage** : Renommage massif de composants et de modules pour harmoniser le vocabulaire technique (ex: passage de "Flow" à "Questionnaire").
