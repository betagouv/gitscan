## Changelog : ecobalyse (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'enrichissement des données (nouveaux objets et secteurs), l'amélioration de l'expérience utilisateur (nouvel éditeur et recherche plus rapide) et le renforcement de la sécurité et de la stabilité technique du système.

### Évolutions fonctionnelles
**Nouvelles fonctionnalités**
- Nouvel éditeur modal pour les éléments d'articles de production ([#2849](https://github.com/MTES-MCT/ecobalyse/issues/2849))
- Possibilité d'édition en masse des articles de production ([#2902](https://github.com/MTES-MCT/ecobalyse/issues/2902))
- Enrichissement de la base de données : ajout de moteurs électriques ([#2846](https://github.com/MTES-MCT/ecobalyse/issues/2846)), d'ingrédients/composants Koch ([#2836](https://github.com/MTES-MCT/ecobalyse/issues/2836)) et d'exemples pour tous les secteurs ([#2897](https://github.com/MTES-MCT/ecobalyse/issues/2897))
- Préparation des secteurs d'objets pour les outils produits ([#2906](https://github.com/MTES-MCT/ecobalyse/issues/2906))

**Améliorations et corrections**
- Amélioration des performances de recherche dans l'explorateur ([#2915](https://github.com/MTES-MCT/ecobalyse/issues/2915))
- Amélioration de l'ergonomie (UX) des champs numériques et de la gestion des noms d'articles ([#2910](https://github.com/MTES-MCT/ecobalyse/issues/2910), [#2855](https://github.com/MTES-MCT/ecobalyse/issues/2855))
- Corrections de données (textile, caractérisations, transport laitier) ([#2892](https://github.com/MTES-MCT/ecobalyse/issues/2892), [#2786](https://github.com/MTES-MCT/ecobalyse/issues/2786), [#2856](https://github.com/MTES-MCT/ecobalyse/issues/2856))

### Évolutions techniques
**Sécurité et Core**
- Sécurité : correction de vulnérabilités ([#2917](https://github.com/MTES-MCT/ecobalyse/issues/2917)) et suppression du cache de jetons ([#2807](https://github.com/MTES-MCT/ecobalyse/issues/2807))
- API & Core : amélioration du format de réponse du simulateur ([#2867](https://github.com/MTES-MCT/ecobalyse/issues/2867)), gestion des portées (scopes) multiples pour les composants ([#2916](https://github.com/MTES-MCT/ecobalyse/issues/2916)) et application des origines par défaut ([#2857](https://github.com/MTES-MCT/ecobalyse/issues/2857))

**Infrastructure et Maintenance**
- Infrastructure & Tests : stabilisation des tests de bout en bout (E2E) ([#2876](https://github.com/MTES-MCT/ecobalyse/issues/2876), [#2858](https://github.com/MTES-MCT/ecobalyse/issues/2858)) et correction du déploiement de `score_history` ([#2912](https://github.com/MTES-MCT/ecobalyse/issues/2912))
- Maintenance : suppression du module admin ([#2870]), simplification de la configuration (clé `TRANSCRYPT_KEY` désormais optionnelle) ([#2872](https://github.com/MTES-MCT/ecobalyse/issues/2872)) et optimisation des processus LCI ([#2894](https://github.com/MTES-MCT/ecobalyse/issues/2894))

### Autres changements
- Documentation des événements plausibles ([#2889](https://github.com/MTES-MCT/ecobalyse/issues/2889))
- Documentation sur l'ajout de nouveaux scopes ([#2839](https://github.com/MTES-MCT/ecobalyse/issues/2839)) et sur les compléments ([#2833](https://github.com/MTES-MCT/ecobalyse/issues/2833))
