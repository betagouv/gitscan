## Changelog : dsfr-skill (30 derniers jours, au 03/11/2026)

### Résumé
Le projet a connu une refonte majeure pour gagner en précision et en fiabilité. Le skill se spécialise désormais sur l'accompagnement HTML et CSS pour les sites de l'État, inclut de nouveaux outils d'audit de conformité et bénéficie d'une automatisation accrue pour rester parfaitement synchronisé avec les évolutions du DSFR.

### Évolutions fonctionnelles
- **Spécialisation de l'usage** : la description du skill est désormais recentrée sur le HTML et le CSS pour éviter toute confusion avec les outils dédiés à React ou à l'audit RGAA. [#6](https://github.com/etalab-ia/dsfr-skill/pull/6)
- **Restriction d'usage** : l'usage du skill est désormais explicitement réservé aux sites de l'État. [#4](https://github.com/etalab-ia/dsfr-skill/pull/4)
- **Nouveaux outils d'aide** : 
    - Ajout d'un guide de démarrage pour la création de pages DSFR.
    - Introduction d'un mode "audit" incluant un vérificateur HTML (détection des identifiants en double, erreurs ARIA, champs sans libellé, etc.).
- **Amélioration des consignes** : les agents sont désormais informés des bonnes pratiques concernant les pictogrammes (interdiction de charger via un CDN externe).

### Évolutions techniques
- **Refonte globale du skill** : régénération complète du contenu basée sur la version 1.15.4 du DSFR. [#3](https://github.com/etalab-ia/dsfr-skill/pull/3)
- **Automatisation de la maintenance** : 
    - Remplacement des anciens scripts de synchronisation Bash par un générateur Node.js. [#5](https://github.com/etalab-ia/dsfr-skill/pull/5)
    - Mise en place d'un workflow ouvrant automatiquement une Pull Request dès qu'une nouvelle version du DSFR est publiée.
- **Renforcement de la CI/CD** : 
    - Vérification automatique de la validité du contenu généré et des liens.
    - Rendu des pages d'évaluation via un navigateur sans interface (headless) pour garantir la qualité des réponses.
- **Évaluation de la performance** : ajout de tests comparatifs pour mesurer l'efficacité réelle du skill sur les réponses des agents IA.

### Autres changements
- **Documentation** : réécriture de `SKILL.md` pour se concentrer sur les erreurs types commises par les agents et mise à jour du README.
- **Traçabilité** : ajout d'un changelog dédié aux versions du plugin.
