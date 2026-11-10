## Changelog : pass-sport (30 derniers jours, au 9 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur grâce à l'automatisation du pré-remplissage des dossiers via FranceConnect. Parallèlement, le projet a renforcé sa robustesse technique avec une refactorisation des traitements de données et une mise à jour majeure de l'infrastructure logicielle pour garantir une meilleure sécurité et performance.

### Évolutions fonctionnelles
- **Simplification des démarches** : Mise en place du pré-remplissage des dossiers pour les utilisateurs connectés via FranceConnect [#694](https://github.com/betagouv/pass-sport/pull/694).
- **Amélioration de l'interface** : Ajout d'un indicateur visuel (label) pour identifier les dossiers pré-remplis et mise à jour de certains textes (wording) pour plus de clarté.
- **Gestion des données** : Intégration de nouveaux flux de données, notamment pour les boursiers Cnous et les bénéficiaires de l'AAH.
- **Mises à jour administratives** : Actualisation de la page des mentions légales et des motifs de contact dans le formulaire [#654](https://github.com/betagouv/pass-sport/pull/654).

### Évolutions techniques
- **Traitement de données** : Refactorisation des scripts de traitement de données vers Python pour une meilleure gestion des flux (Cnous, Grist-DN).
- **Infrastructure et Sécurité** : 
    - Mise à jour majeure de l'environnement (Next.js, Crisp API).
    - Renforcement de la sécurité des versions et durcissement de la sécurité globale.
    - Sécurisation de l'accès au tableau de bord via un chemin secret et l'utilisation de "feature flags".
- **Optimisation système** : 
    - Amélioration de la gestion des erreurs (erreurs 404 et problèmes de cache).
    - Optimisation de la configuration Docker (séparation des stacks WAF et non-WAF).
- **Qualité logicielle** : Corrections diverses sur la suite de tests et amélioration des processus de "dry run" pour les données.

### Autres changements
- Mise à jour de la configuration de monitoring (Sentry).
- Nettoyage de la documentation et de la configuration Ansible.
