## Changelog : territoires-en-transitions (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment une refonte de l'onglet budget des Fiches Actions, l'ajout de la gestion des sous-actions et une amélioration de la navigation et de l'édition des plans. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la gestion des sous-actions : création, édition, suppression et affichage dans le tableau de bord personnel. (#87ce5d3, #802a2da, #6a90b1f, #5225f23, #4ca1383, #2624f36)
- Refonte de l'onglet Budget des Fiches Actions. (#79d0d48)
- Ajout de la possibilité de déplacer des fiches dans le plan. (#1d8e0f2)
- Ajout de la possibilité de modifier la description des axes. (#3bde1c5)
- Amélioration de la gestion des notifications : ajout de notifications "toast" et personnalisation des messages. (#97202e3, #601277a)
- Ajout de l'information COT (Code Type d'Occupation) pour les collectivités et les informations utilisateur. (#ff525e8)
- Possibilité de masquer les boutons d'édition et de suppression pour les fiches confidentielles en mode visite. (#9f81320)
- Ajout d'un bouton pour ouvrir/fermer tous les axes/sous-axes d'un plan. (#df37e39)
- Ajout de la possibilité de lister uniquement les sous-actions. (#a9c0dec)
- Ajout d'indicateurs liés aux axes dans la liste des indicateurs associés à un plan. (#6e6a041)

### Évolutions techniques
- Mise à jour de Next.js pour corriger les vulnérabilités RSC. (#c08fd38)
- Migration vers un nouveau système de rôles et permissions. (#90420cc, #cc27e95, #8e4882f)
- Refactoring de l'import de plan. (#7ec00ab)
- Utilisation de tRPC pour la mise à jour des documents et des commentaires. (#a218361, #f06cf09, #d5e01e8)
- Amélioration des performances des suppressions dans `indicateur_source_metadonnee`. (#6c25968)
- Suppression de l'utilisation de `luxon` et remplacement par des alternatives plus légères. (#2e8d683, #17867e8)
- Mise à jour des dépendances : Supabase, Storybook, Nx, Vite, TypeScript. (#57ae963, #89425dc, #2825f81)
- Migration vers echarts pour les graphiques. (#07fca89, #6e065c1, #5bb462f)
- Suppression du CSS DSFR et remplacement par des composants du design system. (#35bd0c2, #f95d3f0)

### Autres changements
- Ajout de tests e2e pour les nouvelles fonctionnalités. (#a0cc8b8, #7727929, #24dcf7e)
- Amélioration de la documentation et des messages d'erreur. (#5ef9207, #0ea2709)
- Correction de bugs mineurs et améliorations de la qualité du code. (#d245874, #d440905, #6fafe12, #fec4efc, #4eb0a84)
- Ajout de variables d'environnement pour configurer le délai d'envoi des notifications. (#e9761a5)
- Ajout de la gestion des préférences utilisateur (notifications, etc.). (#cfb7699, #b9e0418, #8f5f44e, #de2997d)
- Suppression des tests e2e défaillants pour les actions commentaires. (#d440905)
- Suppression de code non utilisé. (#2f6c38d, #558a2e7)
- Amélioration de la gestion des erreurs et des logs. (#3ca7b83, #361d6ba)
- Ajout de tests unitaires et d'intégration. (#40c2049)
- Correction de problèmes de typage. (#83e592d)
- Amélioration de la gestion des permissions. (#9817db5)
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
