## Changelog : approbiom (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'ajout de plusieurs nouveaux outils (widgets) dédiés à l'importation de données ADEME, à l'analyse technique et à la saisie manuelle. L'expérience utilisateur a été considérablement affinée pour offrir plus de clarté (nouveaux flux de validation, interface plus compacte) et les processus d'importation de données ont été renforcés pour être plus robustes et flexibles face à des fichiers variés.

### Évolutions fonctionnelles
- **Nouveaux widgets :**
    - Mise en place du widget d'importation ADEME [#24](https://github.com/betagouv/approbiom/issues/24).
    - Création du widget d'analyse technique pour comparer deux états ou documents [#25](https://github.com/betagouv/approbiom/issues/25).
    - Développement du widget approvisionnements-plan [#27](https://github.com/betagouv/approbiom/issues/27).
    - Ajout des widgets de recherche d'entreprise et de saisie manuelle des approvisionnements.
- **Amélioration de l'import de documents [#28](https://github.com/betagouv/approbiom/issues/28) :** Nouveau flux de travail incluant des boutons de validation plus explicites ("Voir/Modifier", "Valider") et des alertes en cas de détection de documents déjà extraits.
- **Optimisation de l'interface (UI/UX) :**
    - Recherche insensible aux accents et amélioration de la sélection des fournisseurs.
    - Interface plus compacte pour la gestion de la concurrence.
    - Clarification de l'accueil avec l'ajout de l'année dans les titres de chronologie.
- **Cartographie :** Intégration des fonds de plan IGN et ajustement dynamique de l'opacité des polygones en fonction du tonnage.

### Évolutions techniques
- **Robustesse des scripts d'import (BCIB/BCIAT) :** Amélioration significative de la détection automatique des colonnes (fournisseur, ressource, tonnage) et gestion des formats de fichiers ou de noms de feuilles non standards [#22](https://github.com/betagouv/approbiom/issues/22).
- **Performances :** 
    - Optimisation du chargement des métadonnées sur la page d'accueil.
    - Mise en place du chargement différé (*lazy-loading*) des pièces jointes pour alléger l'affichage.
- **Refonte de l'architecture :** Réorganisation structurelle des composants React (création d'un dossier `hooks`, déplacement des composants) et suppression des scripts Python obsolètes pour simplifier la maintenance.

### Autres changements
- **Documentation :** Mise à jour du guide de développement et des fichiers README des widgets.
- **Nettoyage :** Suppression de dossiers obsolètes et de fichiers de configuration non suivis.
